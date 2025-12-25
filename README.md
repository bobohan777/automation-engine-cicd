# � CI/CD Pipeline (Docker Hub Edition)

## 📖 Project Overview

**Why this lab?**
This project demonstrates a complete **"Commit-to-Container-Registry"** workflow, a fundamental skill for any Cloud Native engineer. It automates the journey of code from a local developer machine to a public Docker Hub registry, ensuring quality and security at every step.

**The Problem it Solves:**
In manual workflows, "it works on my machine" is a common issue. Manual builds are slow, error-prone, and often lack security checks.

**The Solution:**
This **Automation Engine** ensures that:
1.  **Code is Verified**: Automated tests and strict linting (Pylint/Black) run on every commit.
2.  **Security is Built-in**: "Shift-Left" security scans (Trivy/Bandit) block vulnerabilities before they merge.
3.  **Delivery is Automated**: A clean, verified Docker image is automatically built and pushed to Docker Hub, ready for deployment anywhere.

**Key Features:**
- 🐍 **Python/Flask**: A modern microservice application.
- 🐳 **Docker**: Multi-stage builds for small, secure images.
- 🔄 **GitHub Actions**: Zero-maintenance CI/CD pipelines.
- 🛡️ **Trivy & Bandit**: Industry-standard security scanners.

## 📋 Prerequisites

### Required Accounts
- ✅ **GitHub Account** (free)
- ✅ **Docker Hub Account** (free)

### Required Tools (for local development)
- ✅ **Docker Desktop**
- ✅ **Python 3.11** (optional, for local testing)

## 🏗️ Step-by-Step Setup

### **Step 1: GitHub Repository Setup** (2 minutes)

#### 1.1 Fork Repository
1. Fork this repository to your GitHub account.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/automation-engine-cicd.git
   cd automation-engine-cicd
   ```

#### 1.2 Configure GitHub Secrets
Go to: **Settings → Secrets and variables → Actions**

Add these secrets using your Docker Hub credentials:
```
DOCKER_USERNAME=your-dockerhub-username
DOCKER_PASSWORD=your-dockerhub-access-token (or password)
```
> **Tip**: It is best practice to use a Docker Hub **Access Token** instead of your real password.

### **Step 2: Trigger the Pipeline** (1 minute)

#### 2.1 Trigger Deployment
The Deployment pipeline (`cd.yml`) runs automatically on pushes to `main`.

```bash
# Make a small change
echo "Triggering build" >> trigger.txt

# Commit and Push
git add .
git commit -m "🚀 Trigger Docker Hub Pipeline"
git push origin main
```

#### 2.2 Verify Success
1. Go to the **Actions** tab in your repository.
2. Watch the **� CD Pipeline** run.
3. Once green, check your Docker Hub repository.
   - You should see a new image tagged with the commit SHA and `latest`.

### **Step 3: Run Locally (Docker Compose)** (Optional)

You can run the full stack locally using Docker Compose.

```bash
# Start the application
docker compose up -d --build

# Verify it's running
curl http://localhost:5000/health
```

### **Step 4: Deploy to Kubernetes** (Optional)

If you have a Kubernetes cluster ready, you can deploy the manifests.

```bash
# Apply Kubernetes manifests
kubectl apply -f k8s/

# Verify Deployment
kubectl get pods -n automation-engine
```
> **Note**: Ensure you update the image name in `k8s/deployment.yaml` if you are using your own Docker Hub repository.

## � Pipeline Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   📝 Code Push   │───▶│   🔄 CI Pipeline│───▶│   🚀 CD Pipeline│
│                 │    │                 │    │                 │
│ • App Changes   │    │ • Lint & Format │    │ • Build Image   │
│ • Config Updates│    │ • Unit Tests    │    │ • Login to Hub  │
│                 │    │ • Security Scan │    │ • Push Image    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Container Registry** | Docker Hub | Public image storage |
| **Containers** | Docker | Application runtime |
| **CI/CD** | GitHub Actions | Automated pipelines |
| **Security** | Trivy | Container vulnerability scanning |
| **Code Quality** | Pylint / Black | Python standards |
| **Application** | Python Flask | Demo web service |

## 🚀 Advanced Features

### Security Scanning
- **Bandit**: Scans Python code for security issues.
- **Trivy**: Scans the Docker image for OS vulnerabilities before pushing.

### Multi-Architecture Builds
- The pipeline uses `docker buildx` to build images for both `amd64` (Intel/AMD) and `arm64` (Apple Silicon) architectures.

## 🧹 Resource Cleanup

To avoid clutter, follow these steps to clean up resources after your lab.

### Local Docker Cleanup (If you ran Step 3)
```bash
# Stop and remove containers
docker compose down

# Remove local images
docker rmi automation-engine:latest
```

### Kubernetes Cleanup (If you ran Step 4)
```bash
# Delete all resources (Deployment, Service, ConfigMap)
kubectl delete -f k8s/
```

### Docker Hub Cleanup (If you ran Step 2)
1. Log in to [Docker Hub](https://hub.docker.com/).
2. Go to your `automation-engine` repository.
3. Keep the most recent stable tag and delete old experiment tags to save space.

## 🎉 Success Metrics

### Portfolio Value
- ✅ **Automated Container Delivery**: From code to registry in minutes.
- ✅ **Security First**: Integrated security gates prevents bad code from shipping.
- ✅ **Standardization**: Enforced code style and testing.

### Interview Talking Points
- **CI/CD Best Practices**: Separating CI (Test) and CD (Deliver).
- **Containerization**: Writing efficient Dockerfiles.
- **Security**: "Shift Left" security with automated scanning.

---

**🎯 Result**: A clean, automated pipeline delivering high-quality containers to the world's standard registry.

**⏱️ Setup Time**: ~5 minutes
