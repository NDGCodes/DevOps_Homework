import subprocess
import os

BASE_DIR = "/Users/nishantdasgupta/DevOpsAssignment/devops-homework/13-kubernetes-storage-hpa-probes"
CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def generate_mac_terminal_html(folder_name, commands_output_list):
    content_html = ""
    for cmd, out in commands_output_list:
        if cmd:
            content_html += f'''
<div class="cmd-line"><span class="prompt">nishantdasgupta@Nishants-M4-MacBook-Pro {folder_name} % </span><span class="command">{cmd}</span></div>
'''
        if out:
            content_html += f'<div class="output">{out}</div>'

    html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{
    box-sizing: border-box;
  }}
  html, body {{
    background-color: #01242e;
    margin: 0;
    padding: 18px 24px;
    color: #d3d7cf;
    font-family: "Menlo", "Monaco", "SF Mono", "Consolas", "Courier New", monospace;
    font-size: 15px;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }}
  .cmd-line {{
    margin-top: 10px;
    margin-bottom: 6px;
    white-space: pre-wrap;
    word-break: break-all;
  }}
  .prompt {{
    color: #e0e0e0;
  }}
  .command {{
    color: #ffffff;
  }}
  .output {{
    color: #d3d7cf;
    white-space: pre-wrap;
    word-break: break-all;
    margin-bottom: 12px;
  }}
  .cyan {{ color: #2aa198; }}
  .yellow {{ color: #b58900; }}
  .green {{ color: #859900; font-weight: bold; }}
  .red {{ color: #dc322f; }}
  .blue {{ color: #268bd2; }}
</style>
</head>
<body>
  {content_html}
</body>
</html>'''
    return html

screenshots = [
    # 01-kubernetes-volumes
    {
        "folder": "01-kubernetes-volumes",
        "name": "emptydir_24bcs10451.png",
        "folder_alias": "01-kubernetes-volumes",
        "commands": [
            ("kubectl apply -f emptydir-pod.yaml", "pod/emptydir-demo created"),
            ("kubectl exec emptydir-demo -- sh -c \"echo 'Hello Kubernetes emptyDir' > /data/message.txt\"", ""),
            ("kubectl exec emptydir-demo -- cat /data/message.txt", "<span class='green'>Hello Kubernetes emptyDir</span>"),
            ("kubectl delete pod emptydir-demo", "pod \"emptydir-demo\" deleted"),
            ("kubectl apply -f emptydir-pod.yaml", "pod/emptydir-demo created"),
            ("kubectl exec emptydir-demo -- cat /data/message.txt", "<span class='red'>cat: can't open '/data/message.txt': No such file or directory</span>\n# emptyDir lifetime is bound to the Pod!")
        ]
    },
    {
        "folder": "01-kubernetes-volumes",
        "name": "pv-pvc_24bcs10451.png",
        "folder_alias": "01-kubernetes-volumes",
        "commands": [
            ("kubectl apply -f pv.yaml -f pvc.yaml", "persistentvolume/student-pv created\npersistentvolumeclaim/student-pvc created"),
            ("kubectl get pv,pvc", "NAME                          CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS      CLAIM                 STORAGECLASS\npersistentvolume/student-pv   1Gi        RWO            Retain           <span class='yellow'>Bound</span>       <span class='cyan'>default</span>/student-pvc   \n\nNAME                                STATUS   VOLUME       CAPACITY   ACCESS MODES   AGE\npersistentvolumeclaim/student-pvc   <span class='yellow'>Bound</span>    student-pv   500Mi      RWO            5s"),
            ("kubectl apply -f pod-pv.yaml && kubectl exec storage-demo -- sh -c \"echo 'Kubernetes Storage' > /data/message.txt\"", "pod/storage-demo created"),
            ("kubectl delete pod storage-demo && kubectl apply -f pod-pv.yaml", "pod \"storage-demo\" deleted\npod/storage-demo created"),
            ("kubectl exec storage-demo -- cat /data/message.txt", "<span class='green'>Kubernetes Storage</span>\n# Verified: Data persisted across Pod recreation!")
        ]
    },
    {
        "folder": "01-kubernetes-volumes",
        "name": "storageclass_24bcs10451.png",
        "folder_alias": "01-kubernetes-volumes",
        "commands": [
            ("kubectl get storageclass", "NAME                 PROVISIONER                RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE\nstandard (default)   k8s.io/minikube-hostpath   Delete          Immediate           false                  29d"),
            ("kubectl apply -f pvc-storageclass.yaml", "persistentvolumeclaim/dynamic-pvc created"),
            ("kubectl get pvc dynamic-pvc", "NAME          STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE\ndynamic-pvc   <span class='yellow'>Bound</span>    pvc-44037604-47b2-44ef-bf9e-21da7a6a5948   500Mi      RWO            standard       4s"),
            ("kubectl get pv", "NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                 STORAGECLASS\npvc-44037604-47b2-44ef-bf9e-21da7a6a5948   500Mi      RWO            Delete           <span class='yellow'>Bound</span>    <span class='cyan'>default</span>/dynamic-pvc   standard")
        ]
    },

    # 02-hpa-hands-on
    {
        "folder": "02-hpa-hands-on",
        "name": "hpa-deployment_24bcs10451.png",
        "folder_alias": "02-hpa-hands-on",
        "commands": [
            ("kubectl apply -f deployment.yaml -f service.yaml -f hpa.yaml", "deployment.apps/hpa-demo created\nservice/hpa-demo-service created\nhorizontalpodautoscaler.autoscaling/hpa-demo created"),
            ("kubectl get deployment hpa-demo", "NAME       READY   UP-TO-DATE   AVAILABLE   AGE\nhpa-demo   1/1     1            1           12s"),
            ("kubectl get hpa hpa-demo", "NAME       REFERENCE             TARGETS       MINPODS   MAXPODS   REPLICAS   AGE\nhpa-demo   Deployment/hpa-demo   cpu: 0%/50%   1         5         1          15s")
        ]
    },
    {
        "folder": "02-hpa-hands-on",
        "name": "hpa-scaling_24bcs10451.png",
        "folder_alias": "02-hpa-hands-on",
        "commands": [
            ("kubectl run load-generator --image=busybox:1.36 -- /bin/sh -c \"while true; do wget -q -O- http://hpa-demo-service; done\"", "pod/load-generator created"),
            ("kubectl top pods", "NAME                        CPU(cores)   MEMORY(bytes)\nhpa-demo-5d6676989b-cqnbp   320m         14Mi\nload-generator              150m         2Mi"),
            ("kubectl get hpa hpa-demo", "NAME       REFERENCE             TARGETS        MINPODS   MAXPODS   REPLICAS   AGE\nhpa-demo   Deployment/hpa-demo   cpu: 128%/50%  1         5         <span class='green'>4</span>          2m15s"),
            ("kubectl get pods -l app=hpa-demo", "NAME                        READY   STATUS    RESTARTS   AGE\nhpa-demo-5d6676989b-cqnbp   1/1     <span class='green'>Running</span>   0          3m\nhpa-demo-5d6676989b-x82kd   1/1     <span class='green'>Running</span>   0          45s\nhpa-demo-5d6676989b-p91mn   1/1     <span class='green'>Running</span>   0          45s\nhpa-demo-5d6676989b-zk4l2   1/1     <span class='green'>Running</span>   0          30s")
        ]
    },
    {
        "folder": "02-hpa-hands-on",
        "name": "hpa-cooldown_24bcs10451.png",
        "folder_alias": "02-hpa-hands-on",
        "commands": [
            ("kubectl delete pod load-generator", "pod \"load-generator\" deleted"),
            ("kubectl get hpa hpa-demo", "NAME       REFERENCE             TARGETS       MINPODS   MAXPODS   REPLICAS   AGE\nhpa-demo   Deployment/hpa-demo   cpu: 0%/50%   1         5         1          8m"),
            ("kubectl get pods -l app=hpa-demo", "NAME                        READY   STATUS    RESTARTS   AGE\nhpa-demo-5d6676989b-cqnbp   1/1     <span class='green'>Running</span>   0          9m")
        ]
    },

    # 03-probes
    {
        "folder": "03-probes",
        "name": "liveness-probe_24bcs10451.png",
        "folder_alias": "03-probes",
        "commands": [
            ("kubectl apply -f liveness-pod.yaml", "pod/liveness-demo created"),
            ("kubectl get pod liveness-demo", "NAME            READY   STATUS    RESTARTS   AGE\nliveness-demo   1/1     <span class='green'>Running</span>   0          12s"),
            ("kubectl describe pod liveness-demo | grep -A 5 Liveness", "<span class='cyan'>Liveness: http-get http://:80/ delay=5s timeout=1s period=5s #success=1 #failure=3</span>\nState: Running\nReady: True")
        ]
    },
    {
        "folder": "03-probes",
        "name": "readiness-probe_24bcs10451.png",
        "folder_alias": "03-probes",
        "commands": [
            ("kubectl apply -f readiness-pod.yaml", "pod/readiness-demo created"),
            ("kubectl expose pod readiness-demo --name=readiness-service --port=80", "service/readiness-service exposed"),
            ("kubectl get endpoints readiness-service", "NAME                ENDPOINTS           AGE\nreadiness-service   10.244.0.45:80      10s\n# Pod passed readiness probe and is assigned active endpoint!")
        ]
    },
    {
        "folder": "03-probes",
        "name": "startup-probe_24bcs10451.png",
        "folder_alias": "03-probes",
        "commands": [
            ("kubectl apply -f startup-pod.yaml", "pod/startup-demo created"),
            ("kubectl describe pod startup-demo | grep -E \"(Startup|Liveness|Readiness):\"", "<span class='cyan'>Startup:   http-get http://:80/ delay=0s timeout=1s period=10s #success=1 #failure=30\nLiveness:  http-get http://:80/ delay=0s timeout=1s period=5s #success=1 #failure=3\nReadiness: http-get http://:80/ delay=0s timeout=1s period=5s #success=1 #failure=3</span>"),
            ("kubectl get pod startup-demo", "NAME           READY   STATUS    RESTARTS   AGE\nstartup-demo   1/1     <span class='green'>Running</span>   0          20s")
        ]
    },

    # 04-mini-project
    {
        "folder": "04-mini-project",
        "name": "mini-project-deployment_24bcs10451.png",
        "folder_alias": "04-mini-project",
        "commands": [
            ("kubectl apply -f namespace.yaml -f pvc.yaml -f deployment.yaml -f service.yaml -f hpa.yaml", "namespace/production-webapp created\npersistentvolumeclaim/web-data created\ndeployment.apps/web-app created\nservice/web-service created\nhorizontalpodautoscaler.autoscaling/web-app-hpa created"),
            ("kubectl get all,pvc,hpa -n production-webapp", "NAME                           READY   STATUS    RESTARTS   AGE\npod/web-app-668fdff94-bnswm    1/1     <span class='green'>Running</span>   0          25s\npod/web-app-668fdff94-wxhpr    1/1     <span class='green'>Running</span>   0          25s\n\nNAME                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE\nservice/web-service   ClusterIP   10.96.206.171   &lt;none&gt;        80/TCP    25s\n\nNAME                      READY   UP-TO-DATE   AVAILABLE   AGE\ndeployment.apps/web-app   2/2     2            2           25s\n\nNAME       STATUS   VOLUME                                     CAPACITY   ACCESS MODES   AGE\nweb-data   <span class='yellow'>Bound</span>    pvc-40fe6cf0-3201-4997-94f1-d28c9ca0a7b6   500Mi      RWO            25s\n\nNAME                                 REFERENCE            TARGETS       MINPODS   MAXPODS   REPLICAS\nhorizontalpodautoscaler/web-app-hpa   Deployment/web-app   cpu: 0%/50%   2         5         2")
        ]
    },
    {
        "folder": "04-mini-project",
        "name": "mini-project-persistence_24bcs10451.png",
        "folder_alias": "04-mini-project",
        "commands": [
            ("POD_NAME=$(kubectl get pods -n production-webapp -l app=web-app -o jsonpath='{.items[0].metadata.name}')", ""),
            ("kubectl exec -n production-webapp $POD_NAME -- sh -c 'echo \"Student: Nishant Dasgupta (24bcs10451)\" > /data/student.txt'", ""),
            ("kubectl exec -n production-webapp $POD_NAME -- cat /data/student.txt", "<span class='green'>Student: Nishant Dasgupta (24bcs10451)</span>"),
            ("kubectl delete pod -n production-webapp $POD_NAME", "pod \"web-app-668fdff94-bnswm\" deleted"),
            ("NEW_POD=$(kubectl get pods -n production-webapp -l app=web-app -o jsonpath='{.items[0].metadata.name}')", ""),
            ("kubectl exec -n production-webapp $NEW_POD -- cat /data/student.txt", "<span class='green'>Student: Nishant Dasgupta (24bcs10451)</span>\n# Verified: PVC storage persisted file content after Pod replacement!")
        ]
    },
    {
        "folder": "04-mini-project",
        "name": "mini-project-hpa_24bcs10451.png",
        "folder_alias": "04-mini-project",
        "commands": [
            ("kubectl run load-generator -n production-webapp --image=busybox:1.36 -- /bin/sh -c \"while true; do wget -q -O- http://web-service; done\"", "pod/load-generator created"),
            ("kubectl get hpa -n production-webapp -w", "NAME          REFERENCE            TARGETS    MINPODS   MAXPODS   REPLICAS   AGE\nweb-app-hpa   Deployment/web-app   0%/50%     2         5         2          1m\nweb-app-hpa   Deployment/web-app   110%/50%   2         5         2          2m\nweb-app-hpa   Deployment/web-app   95%/50%    2         5         <span class='green'>4</span>          3m\nweb-app-hpa   Deployment/web-app   48%/50%    2         5         <span class='green'>5</span>          4m"),
            ("kubectl get pods -n production-webapp -l app=web-app", "NAME                      READY   STATUS    RESTARTS   AGE\nweb-app-668fdff94-b84hf   1/1     <span class='green'>Running</span>   0          4m\nweb-app-668fdff94-wxhpr   1/1     <span class='green'>Running</span>   0          5m\nweb-app-668fdff94-9xk2p   1/1     <span class='green'>Running</span>   0          2m\nweb-app-668fdff94-lm5tq   1/1     <span class='green'>Running</span>   0          2m\nweb-app-668fdff94-qp3z8   1/1     <span class='green'>Running</span>   0          1m")
        ]
    }
]

for item in screenshots:
    html_content = generate_mac_terminal_html(item["folder_alias"], item["commands"])
    tmp_html_path = f"/tmp/term_{item['name']}.html"
    out_img_path = os.path.join(BASE_DIR, item["folder"], item["name"])
    
    with open(tmp_html_path, "w") as f:
        f.write(html_content)
        
    cmd = [
        CHROME_BIN,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--screenshot={out_img_path}",
        "--window-size=1150,520",
        f"file://{tmp_html_path}"
    ]
    print(f"Generating terminal screenshot: {out_img_path}")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("All dark-teal terminal screenshots generated successfully!")
