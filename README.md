# 🚀 The Automation Engine - CI/CD Pipeline Demo

**"Prove you're a DevOps Engineer, not just a SysAdmin"**

> **Note:** After forking this repository, add your own GitHub Actions badges by replacing `YOUR_USERNAME` with your GitHub username in the badge URLs below.

**Cost:** $0.00 (GitHub Actions + Docker Hub free tiers)

## 🎯 Project Overview

This project demonstrates a **complete CI/CD pipeline** using modern DevOps practices. Perfect for showcasing your skills to employers!

### ✨ What This Demonstrates:
- **Continuous Integration:** Automated testing, linting, and security scanning
- **Continuous Deployment:** Automated Docker builds and registry pushes
- **Security Shift-Left:** Vulnerability scanning that fails builds on high-severity issues
- **GitOps:** Infrastructure and deployment as code
- **Quality Gates:** Automated quality enforcement

### 🏆 Business Value
- **Quality Assurance:** Automated testing prevents bugs in production
- **Security First:** Vulnerability scanning catches issues before deployment
- **Fast Delivery:** Automated pipelines reduce deployment time from hours to minutes
- **Reliability:** Consistent, repeatable deployments reduce human error

## 🏗️ Pipeline Architecture

```
                    🔄 CI/CD Pipeline Architecture
    
    📝 Developer          🔍 CI Pipeline              🚀 CD Pipeline
    ┌─────────────┐      ┌─────────────────────────┐   ┌─────────────────────┐
    │   Git Push  │ ───▶ │    GitHub Actions       │──▶│   Deployment        │
    │     or      │      │                         │   │                     │
    │ Pull Request│      │  1️⃣ Code Checkout        │   │  1️⃣ Docker Build    │
    └─────────────┘      │  2️⃣ Python Linting      │   │  2️⃣ Push to Hub     │
                         │  3️⃣ Unit Tests          │   │  3️⃣ Update K8s      │
                         │  4️⃣ Docker Build        │   │  4️⃣ Deploy (GitOps) │
                         │  5️⃣ Security Scan       │   │                     │
                         │     (Trivy)             │   │                     │
                         └─────────────────────────┘   └─────────────────────┘
                                    │                            │
                                    ▼                            ▼
                         ❌ FAIL on High CVEs          ✅ GREEN Checkmarks
                         ✅ PASS continues pipeline    📦 Docker Hub
                                                       ☸️ Kubernetes Ready
```

## 📁 Repository Structure

```
automation-engine-cicd/
├── 📄 README.md                    # This comprehensive guide
├── 📄 .gitignore                   # Git ignore patterns
├── 📄 requirements.txt             # Python dependencies
├── 📄 Dockerfile                   # Container definition
├── 📄 docker-compose.yml           # Local development
│
├── 🐍 app/                         # Python Flask Application
│   ├── main.py                     # Main application
│   ├── config.py                   # Configuration
│   └── utils.py                    # Utility functions
│
├── 🧪 tests/                       # Test Suite
│   ├── test_main.py                # Unit tests
│   ├── test_utils.py               # Utility tests
│   └── conftest.py                 # Test configuration
│
├── ☸️ k8s/                         # Kubernetes Manifests
│   ├── deployment.yaml             # App deployment
│   ├── service.yaml                # Service definition
│   ├── configmap.yaml              # Configuration
│   └── namespace.yaml              # Namespace
│
├── 🔄 .github/workflows/           # CI/CD Pipelines
│   ├── ci.yml                      # Continuous Integration
│   ├── cd.yml                      # Continuous Deployment
│   └── security.yml                # Security scanning
│
└── 🐳 docker/                      # Docker configurations
    ├── Dockerfile.prod             # Production image
    └── .dockerignore               # Docker ignore
```

## 🚀 CI Pipeline (Continuous Integration)

### Trigger Events
- **Pull Request** to main branch
- **Push** to feature branches
- **Manual** workflow dispatch

### Pipeline Steps

#### 1️⃣ Code Quality
```yaml
- name: Lint Python Code
  run: |
    pylint app/ --fail-under=8.0
    black --check app/
    isort --check-only app/
```

#### 2️⃣ Testing
```yaml
- name: Run Unit Tests
  run: |
    pytest tests/ --cov=app --cov-report=xml
    coverage report --fail-under=80
```

#### 3️⃣ Docker Build
```yaml
- name: Build Docker Image
  run: |
    docker build -t automation-engine:${{ github.sha }} .
    docker tag automation-engine:${{ github.sha }} automation-engine:latest
```

#### 4️⃣ Security Scanning
```yaml
- name: Run Trivy Vulnerability Scanner
  run: |
    trivy image --exit-code 1 --severity HIGH,CRITICAL automation-engine:latest
```

**🔒 Security Gate:** Pipeline FAILS if HIGH or CRITICAL vulnerabilities found

## 🚀 CD Pipeline (Continuous Deployment)

### Trigger Events
- **Merge** to main branch
- **Tag** creation (v*.*.*)

### Deployment Steps

#### 1️⃣ Docker Registry
```yaml
- name: Push to Docker Hub
  run: |
    echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
    docker push ${{ secrets.DOCKER_USERNAME }}/automation-engine:${{ github.sha }}
    docker push ${{ secrets.DOCKER_USERNAME }}/automation-engine:latest
```

#### 2️⃣ GitOps Update
```yaml
- name: Update Kubernetes Manifests
  run: |
    sed -i 's|image: .*|image: ${{ secrets.DOCKER_USERNAME }}/automation-engine:${{ github.sha }}|' k8s/deployment.yaml
    git add k8s/deployment.yaml
    git commit -m "Update image to ${{ github.sha }}"
    git push
```

## 🛠️ Technology Stack

| Component | Technology | Purpose | Skills Demonstrated |
|-----------|------------|---------|-------------------|
| **Application** | Python Flask | Web service | Backend development |
| **Testing** | pytest, coverage | Quality assurance | Test-driven development |
| **Linting** | pylint, black, isort | Code quality | Clean code practices |
| **Containerization** | Docker | Packaging | Container best practices |
| **Security** | Trivy | Vulnerability scanning | Security shift-left |
| **CI/CD** | GitHub Actions | Automation | DevOps pipeline design |
| **Registry** | Docker Hub | Image storage | Container registry mgmt |
| **Orchestration** | Kubernetes | Deployment | Cloud-native deployment |
| **GitOps** | Git-based deployment | Infrastructure as Code | Modern deployment patterns |

## 🔒 Security Features

### Vulnerability Scanning
- **Trivy scanner** checks for known CVEs
- **Fails pipeline** on HIGH/CRITICAL vulnerabilities
- **Generates reports** for security review

### Secrets Management
```yaml
secrets:
  DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
  DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
  KUBECONFIG: ${{ secrets.KUBECONFIG }}
```

### Security Best Practices
- **Non-root container** user
- **Minimal base image** (Alpine Linux)
- **No secrets in code** (environment variables)
- **Dependency scanning** in requirements.txt

## 📊 Quality Gates

### Code Quality Requirements
- **Pylint score:** ≥ 8.0/10
- **Test coverage:** ≥ 80%
- **Code formatting:** Black + isort compliance
- **Security scan:** No HIGH/CRITICAL vulnerabilities

### Pipeline Success Criteria
- ✅ All tests pass
- ✅ Code quality meets standards
- ✅ Docker build succeeds
- ✅ Security scan passes
- ✅ Deployment manifests updated

## 🚀 **QUICK START - Get Green Checkmarks in 10 Minutes!**

### **Step 1: Docker Hub Setup** (3 minutes)
1. **Create account:** Go to [hub.docker.com](https://hub.docker.com) → Sign up
2. **Generate token:** Account Settings → Security → New Access Token
   - Name: `github-actions-automation-engine`
   - Permissions: `Read, Write, Delete`
3. **Copy token** - you won't see it again!

### **Step 2: Fork & Configure** (2 minutes)
1. **Fork this repository** on GitHub
2. **Add GitHub Actions badges** (optional but impressive):
   ```markdown
   [![CI Pipeline](https://github.com/YOUR_USERNAME/automation-engine-cicd/actions/# 🚀 The Automation Engine - CI/CD Pipeline Demo

**"Prove you're a DevOps Engineer, not just a SysAdmin"**

> **Note:** After forking this repository, add your own GitHub Actions badges by replacing `YOUR_USERNAME` with your GitHub username in the badge URLs below.

**Cost:** $0.00 (GitHub Actions + Docker Hub free tiers)
