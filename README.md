# DevOps Portfolio: Containerized FastAPI App with CI/CD and Kubernetes

This repository is a **DevOps-focused demo project** that showcases:

- A small **FastAPI** web service with health checks and tests  
- A **Dockerized** application with `docker-compose` for local development  
- **Kubernetes manifests** (Deployment, Service, Namespace)  
- A **GitHub Actions CI/CD pipeline** that:
  - runs tests
  - builds and pushes a Docker image to Docker Hub
  - deploys the app to a Kubernetes cluster

It is designed as a **portfolio project** for job platforms like Upwork or as an example of your DevOps skills.

---

## Architecture Overview

### 1. Application (FastAPI)
- `app/main.py` contains a small API with:
  - `/` — root endpoint returning metadata (hostname, env)
  - `/healthz` — health check endpoint
- `app/tests/test_main.py` contains integration tests using `pytest` and `TestClient`.

### 2. Containerization
- `Dockerfile` builds a production-ready Python image.
- `docker-compose.yml` enables local development with:
  - automatic rebuild
  - environment variables
  - port forwarding

### 3. Kubernetes
Manifests located in `k8s/`:
- **Namespace**: `devops-portfolio`
- **Deployment**:
  - 2 replicas
  - readiness & liveness probes
  - image: `<your-dockerhub-user>/devops-portfolio-web:latest`
- **Service**:
  - ClusterIP
  - port 80 → 8000

### 4. CI/CD (GitHub Actions)
Workflow: `.github/workflows/ci-cd.yml`

Jobs:
1. **tests**
   - Setup Python
   - Install dependencies
   - Run tests with `pytest`

2. **build_and_push** (only on `main`)
   - Login to Docker Hub
   - Build Docker image
   - Push image with tags:
     - `latest`
     - commit SHA

3. **deploy**
   - Load kubeconfig from GitHub Secret
   - Apply all Kubernetes manifests

---

## Getting Started

### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- (Optional) Kubernetes cluster and `kubectl`
- (Optional) Docker Hub account

---

## Run Locally

### 1. Run with Python

```bash
pip install -r app/requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open: http://localhost:8000  
Health: http://localhost:8000/healthz

Run tests:

```bash
pytest app/tests -v
```

---

### 2. Run with Docker Compose

```bash
docker-compose up --build
```

Service: http://localhost:8000

---

## Docker

Build manually:

```bash
docker build -t your-dockerhub-username/devops-portfolio-web:local .
docker run -p 8000:8000 your-dockerhub-username/devops-portfolio-web:local
```

---

## Kubernetes Deployment

### Apply manifests

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Check resources

```bash
kubectl get pods -n devops-portfolio
kubectl get svc -n devops-portfolio
```

Local port-forward:

```bash
kubectl port-forward svc/devops-portfolio-web -n devops-portfolio 8080:80
```

Then open: http://localhost:8080

---

## CI/CD with GitHub Actions

Triggered on:
- push to `main`
- pull request to `main`

### Required GitHub Secrets

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
- `KUBE_CONFIG_DATA` — base64-encoded kubeconfig

Encode kubeconfig:

```bash
cat ~/.kube/config | base64 -w0
```

---

## How to Present This Project on Upwork

You can describe it like this:

> Implemented an end-to-end DevOps demo project, including Dockerized FastAPI application, Kubernetes deployment, and a full GitHub Actions CI/CD pipeline that runs tests, builds Docker images, pushes them to Docker Hub, and deploys to a Kubernetes cluster.

Demonstrates skills in:

- Docker & containerization
- Kubernetes (manifests, probes, Services)
- GitHub Actions CI/CD
- Python testing
- Cloud-native workflows

---

## Future Improvements

- Add Ingress + TLS (Cert-Manager)
- Add Helm chart
- Add Prometheus metrics + Grafana dashboards
- Implement blue-green or canary deployments
- Add staging/production environments

---

## License
MIT
