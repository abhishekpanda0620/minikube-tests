# Observability Stack on Minikube (YAML-based)

This project sets up a full observability stack inside Minikube using **Prometheus**, **Grafana**, **Node Exporter**, and **Alertmanager**—configured entirely using Kubernetes YAML manifests for deep learning and full control.

---

## 📁 Directory Structure

observability-test/
├── Readme.md
├── alert-manager
│   ├── alert-manager.yml
│   ├── config.yaml
│   ├── deployment.yaml
│   └── service.yaml
├── grafana
│   ├── deployment.yaml
│   └── service.yaml
├── node-exporter
│   ├── daemonset.yaml
│   └── service.yaml
└── prometheus
    ├── alert-rules.yml
    ├── config.yaml
    ├── deployment.yaml
    ├── prometheus.yml
    └── service.yaml


---

## 🧰 Tools Used

- **Minikube** for local Kubernetes cluster
- **Prometheus** for metrics collection
- **Grafana** for visualization
- **Node Exporter** for system-level metrics
- **Alertmanager** for sending alerts to Slack
- **kubectl** for managing the cluster
---

## ✅ What This Stack Does

- Scrapes metrics from Prometheus and Node Exporter.
- Visualizes system health using Grafana dashboards.
- Fires alerts when Node Exporter is down.
- Sends alert notifications to a configured Slack channel.

---

## 🔧 Steps to Deploy

1. **Start Minikube**:
```bash 
   minikube start
```
2. **Deploy Prometheus:**

```bash
kubectl apply -f prometheus/
```
3. **Deploy Grafana:**

```bash
kubectl apply -f grafana/
```
4. **Deploy Node Exporter:**
```bash
kubectl apply -f node-exporter/
```
5. **Deploy Alertmanager:**

```bash
kubectl apply -f alert-manager/
```

## 🔎 Access Services

- Prometheus
```bash
kubectl port-forward svc/prometheus-service 9090:9090

```
Visit: http://localhost:9090 

- Grafana
```bash
kubectl port-forward svc/grafana 3000:3000

```
Visit: http://localhost:3000
 - Login 
    - user: admin
    - password: admin
  - Add Prometheus as a data source at `http://prometheus-service.default.svc.cluster.local:9090` 
- Alertmanager:

```bash
kubectl port-forward svc/alertmanager 9093:9093

```
 Visit: http://localhost:9093
   
## 📊 Dashboards
In Grafana, add Prometheus as a data source and import dashboards for:

 - Node Exporter Full
 - Kubernetes cluster monitoring


## 🚨 Alerting
- Alert rules are defined in alert-rules.yml
- Example: Alert when Node Exporter is down
- Alerts are routed to a Slack channel using webhook URL via Alertmanager

## 🧪 Test Alerts
Simulate alert by deleting Node Exporter pod:

```bash
kubectl delete pod <node-exporter-pod-name>
```
An alert should appear in Prometheus and be forwarded to Slack.

If doesn't work try deleting the daemonset 
```bash
kubectl delete daemonset node-exporter
```
PS: Later re apply the `node-exporter/daemonset.yaml` to keep it running


## 📝 Summary
This setup demonstrates a complete observability stack deployed entirely via Kubernetes YAML. It includes real-time metrics scraping with Prometheus, rich visualization via Grafana, system monitoring using Node Exporter, and alerting via Alertmanager integrated with Slack. This project serves as a strong foundation for learning SRE practices, GitOps, and Kubernetes-native monitoring—all while staying infrastructure-agnostic and extensible.
