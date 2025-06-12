# Kustomize Setup

## 🧱 Base Setup

**Directory:** `base/`

* `deployment.yaml`: NGINX Deployment (no env-specific logic)
* `service.yaml`: ClusterIP service
* `kustomization.yaml`: Contains common resources

```yaml
resources:
  - deployment.yaml
  - service.yaml
```

## 🔧 Overlays

**Directory:** `overlays/dev/` or `overlays/prod/`

* Adds environment-specific config and replica patches
* Generates a ConfigMap with HTML content

```yaml
namePrefix: dev-
resources:
  - ../../base

configMapGenerator:
  - name: nginx-config
    literals:
      - index.html=<html><body><h1>Welcome to DEV environment</h1></body></html>

patches:
  - path: replica-patch.yaml
    target:
      kind: Deployment
      name: nginx
```

To apply:

```sh
kubectl apply -k overlays/dev
```

---
