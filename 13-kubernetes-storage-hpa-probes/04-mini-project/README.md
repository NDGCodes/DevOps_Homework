# Task 4: Production-Ready Kubernetes Web App Capstone Mini-Project

Student: Nishant Dasgupta  
Roll Number: **24bcs10451**  
Namespace: `production-webapp`

---

## 1. Project Overview

This capstone project combines the three core pillars of Kubernetes production workloads:
1. **State Persistence**: 500Mi `PersistentVolumeClaim` (`web-data`) attached to `/data` across all workload replicas.
2. **Elastic Scaling**: `HorizontalPodAutoscaler` (`web-app-hpa`) configured to dynamically scale Pod count between 2 and 5 replicas based on a 50% CPU threshold.
3. **Application Health Diagnostics**: Tri-probe health system (`StartupProbe`, `ReadinessProbe`, and `LivenessProbe`) ensuring clean initialization, zero-downtime routing, and auto-healing.

---

## 2. Architecture Diagram

```text
                           [ Service: web-service ]
                                      | (ClusterIP: 80)
                +---------------------+---------------------+
                v                                           v
          [ Pod: web-app-1 ]                          [ Pod: web-app-2 ]
          +- Startup Probe                            +- Startup Probe
          +- Readiness Probe                          +- Readiness Probe
          +- Liveness Probe                           +- Liveness Probe
          +- CPU Request: 100m                        +- CPU Request: 100m
          +---------+-----------------------------------------+----------+
                    |                                         |
                    +--------------------+--------------------+
                                         |
                                         v
                            [ HPA: web-app-hpa (50% CPU) ]
                                         ^
                                         | pulls metrics
                                 [ Metrics Server ]
Pod
 |
 +-- VolumeMount: /data
       |
       +-- PVC: web-data (500Mi, ReadWriteOnce)
             |
             +-- StorageClass: standard (k8s.io/minikube-hostpath)
```

---

## 3. Kubernetes Manifests

### Namespace (`namespace.yaml`)
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production-webapp
```

### PVC (`pvc.yaml`)
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: web-data
  namespace: production-webapp
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: standard
  resources:
    requests:
      storage: 500Mi
```

### Deployment (`deployment.yaml`)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  namespace: production-webapp
spec:
  replicas: 2
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-container
        image: nginx:alpine
        ports:
        - containerPort: 80
        resources:
          limits:
            cpu: 200m
            memory: 256Mi
          requests:
            cpu: 100m
            memory: 128Mi
        startupProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
          failureThreshold: 10
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 10
          periodSeconds: 10
        volumeMounts:
        - name: app-storage
          mountPath: /data
      volumes:
      - name: app-storage
        persistentVolumeClaim:
          claimName: web-data
```

### Service (`service.yaml`) & HPA (`hpa.yaml`)
Exposes port 80 internally and autoscales between 2 and 5 replicas at 50% CPU utilization.

---

## 4. Verification & Execution Results

### Task 4.1: Initial Infrastructure Deployment
I applied all manifests in `production-webapp` namespace. 2 Pods, PVC (`web-data`), Service (`web-service`), and HPA (`web-app-hpa`) initialized cleanly.

![Mini Project Deployment](mini-project-deployment_24bcs10451.png)

### Task 4.2: Data Persistence Across Pod Termination
1. I executed inside `web-app-668fdff94-bnswm` and created file `/data/student.txt` containing `Student: Nishant Dasgupta (24bcs10451)`.
2. I deleted Pod `web-app-668fdff94-bnswm`.
3. I verified replacement Pod `web-app-668fdff94-b84hf` read the exact file `/data/student.txt` with content intact.

![Mini Project Storage Persistence](mini-project-persistence_24bcs10451.png)

### Task 4.3: HPA Elastic Traffic Scaling
I deployed load generator in `production-webapp` namespace. Upon CPU spike to 110%, HPA scaled deployment out to **4 replicas** and then **5 replicas**, distributing load cleanly.

![Mini Project HPA Scaling](mini-project-hpa_24bcs10451.png)

---
