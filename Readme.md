# Minikube Tests
# Minikube Tests

A collection of Kubernetes manifests to demonstrate and test common features on Minikube:

- **statefulset-test**  
    Deploy a PostgreSQL instance backed by a PersistentVolume and Stateful-like behavior.  
    Files:
    - `postgres-pv.yaml` (PV & PVC)
    - `postgres-deploy.yaml` (Deployment + PVC mount)
    - `postgres-service.yaml`
    - `pg-client-deploy.yaml` (interactive client)

- **pv-test**  
    Show how to create a hostPath PersistentVolume and consume it via a PVC in an NGINX Pod.  
    Files:
    - `nginx-pv.yaml` (PV)
    - `nginx-pvc.yaml` (PVC)
    - `nginx-pod.yaml`

- **inspect-pod**  
    Deploy a standalone NGINX Pod and expose it with a NodePort Service for quick inspection.  
    Files:
    - `nginx-deploy.yaml`
    - `nginx-svc.yaml`

- **pvc-test**  
    Test writing data into a PVC from a BusyBox Pod.  
    Files:
    - `pvc.yaml` (PVC)
    - `pvc-deploy.yaml` (Pod that writes to the PVC)

## Prerequisites

- [Minikube](https://minikube.sigs.k8s.io/docs/) installed and running  
- `kubectl` configured to talk to your Minikube cluster

## Usage

1. Navigate into a test directory, e.g.:
        ```bash
        cd statefulset-test
        ```
2. Apply all manifests:
        ```bash
        kubectl apply -f .
        ```
3. Verify resources:
        ```bash
        kubectl get pods,svc,pv,pvc
        ```
4. Clean up:
        ```bash
        kubectl delete -f .
        ```

Feel free to explore each directory and experiment with the manifests to learn how Kubernetes storage and services work on Minikube.