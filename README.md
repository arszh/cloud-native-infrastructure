# Cloud-Native Infrastructure Project

This project demonstrates a complete DevOps lifecycle: from application development to automated CI/CD and deployment into Kubernetes. It showcases key cloud-native practices such as containerization, orchestration, automation, and infrastructure delivery.

---

## 🚀 **Key Features**
- Application containerization using **Docker**
- Local development via **docker-compose**
- Automated CI/CD using **GitHub Actions**
- Image publishing to **Docker Hub**
- Deployment to **Kubernetes** (Deployment, Service, Namespace)
- Simple **FastAPI** web service with tests
- Clean and production-oriented repository structure

---

## 🏗️ **Project Architecture**
```
├── app/                 # FastAPI application + tests
├── k8s/                 # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── namespace.yaml
├── Dockerfile           # Container build
├── docker-compose.yml   # Local environment
├── .github/workflows/   # CI/CD pipeline
│   └── ci-cd.yaml
└── README.md
```

---

## 📦 **Technology Stack**
- **FastAPI** — backend service
- **Pytest** — testing
- **Docker / Docker Compose** — containerization
- **Kubernetes** — orchestration
- **GitHub Actions** — CI/CD automation
- **Docker Hub** — container registry

---

## ⚙️ **CI/CD Pipeline**
### GitHub Actions performs:
1. Dependency installation
2. Running unit tests
3. Building Docker image
4. Pushing image to Docker Hub
5. Deploying updates automatically to Kubernetes

This ensures fast, stable, and automated delivery with zero manual steps.

---

## 📁 **Kubernetes Manifests**
Inside the `k8s/` directory:
- `namespace.yaml` — defines the application namespace
- `deployment.yaml` — main deployment spec with update strategy
- `service.yaml` — exposes the application inside the cluster

Deployment command:
```
kubectl apply -f k8s/
```

---

## ▶️ **Local Development**
### 1. Run with Docker:
```
docker build -t myapp .
docker run -p 8000:8000 myapp
```

### 2. Run via docker-compose:
```
docker-compose up --build
```

Application will be available at:
```
http://localhost:8000
```

---

## 📘 **Testing**
Run tests using:
```
pytest
```

Tests are integrated into CI/CD and must pass before merging.

---

## ☸️ **Kubernetes Deployment**
Ensure your cluster is running and `kubectl` is configured.

Apply manifests:
```
kubectl apply -f k8s/
```

Check status:
```
kubectl get pods -n cloud-native-app
```

