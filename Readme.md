# Minikube Tests

A collection of Kubernetes manifests to demonstrate and test common features on Minikube:

- **statefulset-test**  
    Examples of StatefulSets with persistent storage:
    - **MySQL**:
        - `mysql-statefulset/mysql-statefulset.yaml` (StatefulSet)
        - `mysql-statefulset/mysql-headless.yaml` (Headless Service)
        - `mysql-statefulset/php-app-deployment.yaml` (PHP-Nginx app to connect to MySQL)
        - `mysql-statefulset/php-app-svc.yaml` (Service to expose PHP app)
    - **Redis**:
        - `redis-statefulset/redis-statefulset.yaml` (StatefulSet)
        - `redis-statefulset/redis-headless.yaml` (Headless Service)
    - **NGINX**:
        - `nginx-statefulset/nginx-statefulset.yaml` (StatefulSet)
        - `nginx-statefulset/nginx-headless.yaml` (Headless Service)

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

- **daemonset-test**  
    Deploy a complete monitoring stack on Minikube:  
      - A Flask app exposing Prometheus metrics  
      - Prometheus server (with ConfigMap)  
      - Grafana dashboard  
      - Node Exporter as a DaemonSet  
    Files:  
    - `metric-app.yaml` (Flask metrics app Deployment & Service)  
    - `prometheus-config.yaml` (ConfigMap)  
    - `prometheus-deploy.yaml` (Prometheus Deployment)  
    - `prometheus-svc.yaml` (Prometheus Service)  
    - `grafana.yaml` (Grafana Deployment & Service)  
    - `node-exporter-daemonset.yaml` (Node Exporter DaemonSet)  
    - `node-exporter-service.yaml` (Node Exporter Service)  
    - Custom Flask app with Prometheus metrics in `app/` directory

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

## Features Demonstrated

- **StatefulSets**: Deploying stateful applications with stable network identities and persistent storage
- **PersistentVolumes**: Managing storage in Kubernetes with different provisioners
- **Services**: Exposing applications using ClusterIP and NodePort service types
- **DaemonSets**: Running pods on every node in the cluster
- **ConfigMaps**: Providing configuration to applications
- **Multi-container Pods**: Running multiple containers in a single pod (e.g., PHP-NGINX)

Feel free to explore each directory and experiment with the manifests to learn how Kubernetes storage, services, and monitoring work on Minikube.