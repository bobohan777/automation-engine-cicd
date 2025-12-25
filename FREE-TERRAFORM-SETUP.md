# 🆓 FREE Terraform + Local Kubernetes Lab

## 🎯 What This Demonstrates (Cost: $0.00)

- **Infrastructure as Code** with Terraform
- **Local Kubernetes** with kind/minikube  
- **Docker Registry** simulation
- **CI/CD Pipelines** with GitHub Actions
- **All DevOps skills** without AWS costs

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   📝 Code Push   │───▶│  🏗️ Terraform   │───▶│   🔄 CI/CD      │
│                 │    │                 │    │                 │
│ • App Changes   │    │ • Local K8s     │    │ • Build & Test  │
│ • Infra Changes │    │ • Docker Reg    │    │ • Security Scan │
│ • Config Updates│    │ • Networking    │    │ • Deploy Local  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ Technology Stack

| Component | Technology | Cost |
|-----------|------------|------|
| **Infrastructure** | Terraform + Docker | $0 |
| **Kubernetes** | kind/minikube | $0 |
| **Registry** | Local Docker Registry | $0 |
| **CI/CD** | GitHub Actions | $0 |
| **Monitoring** | Prometheus/Grafana | $0 |

## 🚀 Setup Steps

### 1. Install Tools
```bash
# Install required tools
brew install terraform kubectl kind docker
# or
choco install terraform kubernetes-cli kind docker-desktop
```

### 2. Create Local Infrastructure
```bash
# Use Terraform to provision local resources
terraform init
terraform apply
```

### 3. Deploy Application
```bash
# CI/CD pipeline deploys to local cluster
git push origin main
```

## 🎯 Skills Demonstrated

- ✅ **Terraform IaC** - Infrastructure provisioning
- ✅ **Kubernetes** - Container orchestration  
- ✅ **CI/CD** - Automated pipelines
- ✅ **Security** - Vulnerability scanning
- ✅ **GitOps** - Deployment automation

**Perfect for**: Learning, portfolio, interviews
**Interview Value**: Shows Terraform + K8s skills
**Portfolio Impact**: High (demonstrates IaC knowledge)