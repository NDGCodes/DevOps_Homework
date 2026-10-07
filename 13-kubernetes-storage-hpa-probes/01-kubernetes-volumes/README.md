# Task 1: Kubernetes Volumes & Storage Fundamentals

Student: Nishant Dasgupta  
Roll Number: **24bcs10451**

---

## Overview

Kubernetes provides multiple volume types to handle different data persistence lifecycles:
1. **`emptyDir`**: Temporary storage tied directly to the Pod's lifecycle.
2. **`hostPath`**: Mounts a file or directory from the host node's filesystem into the Pod.
3. **`PersistentVolume` (PV) & `PersistentVolumeClaim` (PVC)**: Decoupled storage resource abstraction allowing persistent data storage independently of Pod lifecycles.
4. **`StorageClass` & Dynamic Provisioning**: Automatically provisions backend PersistentVolumes on demand when a PersistentVolumeClaim is created.

---

## 1. `emptyDir` Volume Demonstration

An `emptyDir` volume is initially empty and is created when a Pod is assigned to a Node. Containers within the same Pod can read and write the same files in the `emptyDir` volume. However, when a Pod is removed from a node for any reason, the data in the `emptyDir` is erased permanently.

### Manifest (`emptydir-pod.yaml`)
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: emptydir-demo
spec:
  containers:
  - name: alpine
    image: alpine:latest
    command: ["sleep", "3600"]
    volumeMounts:
    - name: data-volume
      mountPath: /data
  volumes:
  - name: data-volume
    emptyDir: {}
```

### Observations
1. File `/data/message.txt` with content `Hello Kubernetes emptyDir` was written inside the running container.
2. After deleting the Pod (`kubectl delete pod emptydir-demo`) and recreating it, reading `/data/message.txt` yielded `No such file or directory`.
3. **Conclusion**: `emptyDir` is strictly ephemeral and tied to Pod lifespan.

![emptyDir Pod Evidence](emptydir_24bcs10451.png)

---

## 2. PersistentVolume (PV) & PersistentVolumeClaim (PVC)

`PersistentVolume` (PV) represents physical cluster storage provisioned by an administrator. A `PersistentVolumeClaim` (PVC) is a request for storage by a developer.

### Access Modes Comparison
- **`ReadWriteOnce` (RWO)**: Volume can be mounted as read-write by a single node.
- **`ReadOnlyMany` (ROX)**: Volume can be mounted as read-only by many nodes.
- **`ReadWriteMany` (RWX)**: Volume can be mounted as read-write by many nodes.
- **`ReadWriteOncePod` (RWOP)**: Volume can be mounted as read-write by a single Pod.

### Manifests (`pv.yaml` & `pvc.yaml` & `pod-pv.yaml`)
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: student-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  hostPath:
    path: "/mnt/data/student-pv"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: student-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
```

### Observations
1. The PVC `student-pvc` bound to `student-pv` (`STATUS: Bound`).
2. Data written to `/data/message.txt` remained intact after deleting and recreating `storage-demo` Pod.
3. **Conclusion**: PersistentVolumes guarantee data survival across Pod restarts and redeployments.

![PV and PVC Evidence](pv-pvc_24bcs10451.png)

---

## 3. Dynamic Provisioning with StorageClass

`StorageClass` defines different "classes" of storage (e.g. SSD, HDD, cloud disk). It enables **dynamic provisioning** so admins do not need to manually pre-provision PersistentVolumes.

### Manifest (`pvc-storageclass.yaml`)
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: dynamic-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: standard
  resources:
    requests:
      storage: 500Mi
```

### Observations
- Upon applying `pvc-storageclass.yaml`, Kubernetes automatically invoked the `standard` StorageClass provisioner (`k8s.io/minikube-hostpath`) and dynamically created a new PV named `pvc-44037604-47b2-44ef-bf9e-21da7a6a5948`.

![StorageClass Evidence](storageclass_24bcs10451.png)
