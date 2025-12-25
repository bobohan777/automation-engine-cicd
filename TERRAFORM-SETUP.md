# 🚀 Enhanced CI/CD + Terraform Lab Setup Guide

## 🎯 What This Lab Demonstrates

This enhanced lab showcases **complete DevOps engineering skills**:

- **Infrastructure as Code (IaC)** with Terraform
- **AWS Cloud Services** (EKS, ECR, VPC, IAM)
- **CI/CD Pipelines** with GitHub Actions
- **Container Security** with Trivy scanning
- **GitOps Deployment** patterns
- **Quality Gates** and automated testing

## 📋 Prerequisites

### Required Accounts
- ✅ **GitHub Account** (free)
- ✅ **AWS Account** (free tier eligible)

### Required Tools (for local development)
- ✅ **AWS CLI** v2
- ✅ **Terraform** >= 1.6.0
- ✅ **kubectl** 
- ✅ **Docker Desktop**

## 🏗️ Step-by-Step Setup

### **Step 1: AWS Setup** (10 minutes)

#### 1.1 Create IAM User for Terraform
```bash
# Login to AWS Console
# Go to IAM → Users → Create User
# Username: terraform-automation-engine
# Attach policies:
# - AmazonEKSClusterPolicy
# - AmazonEKSWorkerNodePolicy
# - AmazonEKS_CNI_Policy
# - AmazonEC2ContainerRegistryFullAccess
# - AmazonVPCFullAccess
# - IAMFullAccess (for role creation)
```

#### 1.2 Create Access Keys
```bash
# In IAM User → Security credentials
# Create access key → CLI usage
# Save: Access Key ID and Secret Access Key
```

### **Step 2: GitHub Repository Setup** (5 minutes)

#### 2.1 Fork Repository
```bash
# Fork this repository on GitHub
# Clone your fork locally
git clone https://github.com/YOUR_USERNAME/automation-engine-cicd.git
cd automation-engine-cicd
```

#### 2.2 Configure GitHub Secrets
Go to: **Settings → Secrets and variables → Actions**

Add these secrets:
```
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
```

### **Step 3: Infrastructure Deployment** (15 minutes)

#### 3.1 Deploy Infrastructure
```bash
# Trigger Terraform workflow
# Go to Actions tab → Infrastructure (Terraform)
# Click "Run workflow" → Select "apply"
```

#### 3.2 Verify Infrastructure
```bash
# After successful deployment, check AWS Console:
# - EKS Cluster: automation-engine-cluster
# - ECR Repository: automation-engine
# - VPC with public/private subnets
```

### **Step 4: Application Deployment** (5 minutes)

#### 4.1 Update Kubernetes Deployment
```bash
# Get ECR repository URL from Terraform outputs
# Update k8s/deployment.yaml with your ECR URL
```

#### 4.2 Trigger CI/CD Pipeline
```bash
# Make a small change and push
echo "# Enhanced with Terraform" >> README.md
git add .
git commit -m "🚀 Deploy to AWS EKS with Terraform"
git push origin main
```

## 🔄 Pipeline Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   📝 Code Push   │───▶│  🏗️ Terraform   │───▶│   🔄 CI/CD      │
│                 │    │                 │    │                 │
│ • App Changes   │    │ • EKS Cluster   │    │ • Build & Test  │
│ • Infra Changes │    │ • ECR Registry  │    │ • Security Scan │
│ • Config Updates│    │ • VPC Network   │    │ • Deploy to EKS │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Infrastructure** | Terraform | AWS EKS, ECR, VPC provisioning |
| **Container Registry** | AWS ECR | Secure image storage |
| **Orchestration** | AWS EKS | Kubernetes cluster |
| **CI/CD** | GitHub Actions | Automated pipelines |
| **Security** | Trivy + tfsec | Container & IaC scanning |
| **Application** | Python Flask | Demo web service |

## 📊 Cost Estimation

### AWS Resources (Monthly)
- **EKS Cluster**: ~$73/month
- **EC2 Instances** (2x t3.medium): ~$60/month
- **NAT Gateway**: ~$45/month
- **ECR Storage**: ~$1/month (minimal usage)

**Total**: ~$179/month

### Cost Optimization
- Use **t3.small** instances: Save ~$30/month
- **Single AZ** deployment: Save ~$22/month
- **Spot instances**: Save ~40% on compute

## 🎯 Skills Demonstrated

### Infrastructure Engineering
- ✅ **Terraform IaC** - Complete AWS infrastructure
- ✅ **AWS Services** - EKS, ECR, VPC, IAM
- ✅ **Network Design** - Public/private subnets, NAT gateways
- ✅ **Security** - IAM roles, OIDC integration

### DevOps Engineering
- ✅ **CI/CD Design** - Multi-stage pipelines
- ✅ **Container Security** - Vulnerability scanning
- ✅ **GitOps** - Infrastructure and app deployment
- ✅ **Quality Gates** - Automated testing and validation

### Cloud Architecture
- ✅ **Scalable Design** - Auto-scaling node groups
- ✅ **High Availability** - Multi-AZ deployment
- ✅ **Security Best Practices** - Least privilege access
- ✅ **Cost Optimization** - Resource tagging and lifecycle

## 🚀 Advanced Features

### Monitoring & Observability
```bash
# Add to your infrastructure:
# - CloudWatch logging
# - Prometheus metrics
# - Grafana dashboards
# - AWS X-Ray tracing
```

### Multi-Environment Support
```bash
# Extend with:
# - Dev/Staging/Prod environments
# - Environment-specific configurations
# - Blue/Green deployments
# - Canary releases
```

## 🔧 Troubleshooting

### Common Issues

#### Terraform Apply Fails
```bash
# Check AWS credentials
aws sts get-caller-identity

# Verify IAM permissions
# Ensure all required policies are attached
```

#### EKS Cluster Access
```bash
# Update kubeconfig
aws eks update-kubeconfig --region us-west-2 --name automation-engine-cluster

# Test access
kubectl get nodes
```

#### ECR Push Fails
```bash
# Login to ECR
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-west-2.amazonaws.com
```

## 🎉 Success Metrics

### Portfolio Value
- ✅ **Complete AWS Infrastructure** provisioned with Terraform
- ✅ **Production-ready EKS cluster** with security best practices
- ✅ **Automated CI/CD pipelines** with quality gates
- ✅ **Container security scanning** integrated
- ✅ **GitOps deployment** patterns implemented

### Interview Talking Points
- **Infrastructure as Code** design and implementation
- **AWS cloud architecture** decisions and trade-offs
- **Security integration** throughout the pipeline
- **Cost optimization** strategies
- **Scalability and reliability** considerations

## 📚 Next Steps

### Enhancements
1. **Add monitoring** with Prometheus/Grafana
2. **Implement logging** with ELK stack
3. **Add secrets management** with AWS Secrets Manager
4. **Implement backup** strategies
5. **Add disaster recovery** procedures

### Learning Resources
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [EKS Best Practices](https://aws.github.io/aws-eks-best-practices/)
- [Container Security](https://kubernetes.io/docs/concepts/security/)

---

**🎯 Result**: A complete, production-ready DevOps portfolio demonstrating Infrastructure as Code, CI/CD, and AWS cloud expertise!

**💰 Cost**: ~$179/month (can be optimized to ~$100/month)

**⏱️ Setup Time**: ~35 minutes

**🏆 Skills Level**: Senior DevOps Engineer