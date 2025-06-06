# Kubernetes StatefulSet MySQL + PHP-Nginx Example on Minikube

This guide covers:

- Setting up MySQL using a StatefulSet with persistent storage

- Deploying a PHP-Nginx app using a custom PHP image with mysqli support to connect to MySQL

- Testing connectivity

- Cleanup instructions



## Prerequisites

- Minikube installed and running

- kubectl installed and configured

- Docker installed and logged into Docker Hub


## 1. MySQL StatefulSet Setup

### 1.1 Create a Headless Service for MySQL

```yaml
apiVersion: v1
kind: Service
metadata:
  name: mysql
  labels:
    app: mysql
spec:
  clusterIP: None
  ports:
    - port: 3306
  selector:
    app: mysql

```

This service enables stable network IDs for each MySQL pod (required by StatefulSet).

### 1.2 Create MySQL StatefulSet with Persistent Storage

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mysql
spec:
  serviceName: "mysql"
  replicas: 1
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: rootpassword
        - name: MYSQL_DATABASE
          value: testdb
        ports:
        - containerPort: 3306
          name: mysql
        volumeMounts:
        - name: mysql-persistent-storage
          mountPath: /var/lib/mysql
  volumeClaimTemplates:
  - metadata:
      name: mysql-persistent-storage
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 1Gi

```

apply manifests and check the status using kubectl
```bash
kubectl apply -f mysql-headless.yaml,mysql-statefulset.yaml
kubectl get pods -l app=mysql
kubectl get pvc
```

## 2. PHP-Nginx App Setup

### 2.1 Build and Push Custom PHP Image (with mysqli)


```bash
# From your directory containing Dockerfile
docker build -t abhishek626/php-mysqli:8.2-fpm .

docker login

docker push abhishek626/php-mysqli:8.2-fpm

```

### 2.2 Deploy PHP-Nginx Application

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: php-nginx-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: php-nginx-app
  template:
    metadata:
      labels:
        app: php-nginx-app
    spec:
      containers:
      - name: nginx
        image: nginx:1.25
        ports:
        - containerPort: 80
        volumeMounts:
        - name: code
          mountPath: /var/www/html
        - name: code
          mountPath: /etc/nginx/conf.d/default.conf
          subPath: nginx/default.conf
      - name: php-fpm
        image: abhishek626/php-mysqli:8.2-fpm
        volumeMounts:
        - name: code
          mountPath: /var/www/html
      volumes:
      - name: code
        hostPath:
          path: /mnt/php-app
          type: Directory

```

Deploy the service to expose it using nodeport.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: php-nginx-app
spec:
  type: NodePort
  selector:
    app: php-nginx-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30003

```

Apply Manifests and check status using kubectl 

```bash
kubectl apply -f php-app-deployment.yaml,php-app-svc.yaml
kubectl get pods -l app=php-nginx-app
```
## 3. Test Connection

Access the PHP app

```bash
minikube service php-nginx-app --url
# or curl http://<minikube-ip>:30003/
```
The PHP app (with index.php) should connect to the MySQL StatefulSet service mysql on port 3306.

## 4.Cleanup
```bash
kubectl delete -f php-app-svc.yaml
kubectl delete -f php-app-deployment.yaml
kubectl delete -f mysql-statefulset.yaml
kubectl delete -f mysql-headless.yaml
docker rmi abhishek626/php-mysqli:8.2-fpm

```

## 🧩 Summary
This project sets up a complete local development environment on Minikube featuring:

- 🐬 MySQL StatefulSet with persistent storage and stable network identity

- 🐘 PHP app connected to MySQL, served via Nginx

- 🐳 Custom Docker image for PHP with mysqli support

- 📦 Kubernetes-native deployment using Deployment, StatefulSet, and Service resources

- 🧼 One-liner cleanup to remove all resources when done

🔁 A practical example of deploying a stateful backend and a dynamic frontend on Kubernetes, ideal for learning, testing, or demonstrating cloud-native patterns!