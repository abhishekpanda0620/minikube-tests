
# Helm Setup

## 📁 Helm Chart Structure

```bash
helm-test/
├── Chart.yaml
├── values.yaml
├── dev-values.yaml
├── prod-values.yaml
└── templates/
    ├── configmap.yaml
    ├── deployment.yaml
    ├── service.yaml
    └── NOTES.txt
```

## 🔧 `values.yaml`

```yaml
replicaCount: 1
htmlContent: "<html><body><h1>Welcome to ENV environment</h1></body></html>"
service:
  type: ClusterIP
  port: 80
```

## 🌐 Custom Values per Env

**`dev-values.yaml`**

```yaml
htmlContent: "<html><body><h1>Welcome to DEV environment</h1></body></html>"
```

**`prod-values.yaml`**

```yaml
htmlContent: "<html><body><h1>Welcome to PROD environment</h1></body></html>"
```

## ⬇️ Install Helm Releases

```sh
helm install dev-nginx . -f dev-values.yaml
helm install prod-nginx . -f prod-values.yaml
```

## 🔁 Common Issues

* `ConfigMap already exists`: Uninstall existing Helm release or use unique names
* Port conflicts when forwarding (use different local ports)

---

# Ingress Setup

## 📦 Install NGINX Ingress Controller

```sh
minikube addons enable ingress
```

## 🚪 Define Ingress Rules

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: dev-nginx-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
    - host: dev.local
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: dev-nginx-service
                port:
                  number: 80
```

Same for `prod.local`



## 🖥️ Local DNS Setup
Find minikube ip address
```bash
minikube ip
```
if its `192.168.49.2`

Add this to `/etc/hosts` (in WSL/linux or host system,it requires `sudo` access):

```bash
192.168.49.2 dev.local
192.168.49.2 prod.local
```


## 🌐 Access

```sh
curl http://dev.local    # shows DEV environment
curl http://prod.local   # shows PROD environment
```

---
