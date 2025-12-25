terraform {
  required_version = ">= 1.0"
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# Local Docker Registry
resource "docker_container" "registry" {
  name  = "local-registry"
  image = "registry:2"
  
  ports {
    internal = 5000
    external = 5000
  }
  
  restart = "unless-stopped"
  
  labels {
    label = "automation-engine.component"
    value = "registry"
  }
}

# Local Kubernetes Cluster (kind)
resource "local_file" "kind_config" {
  filename = "${path.module}/kind-config.yaml"
  content = yamlencode({
    kind = "Cluster"
    apiVersion = "kind.x-k8s.io/v1alpha4"
    containerdConfigPatches = [
      <<-EOF
      [plugins."io.containerd.grpc.v1.cri".registry.mirrors."localhost:5000"]
        endpoint = ["http://localhost:5000"]
      EOF
    ]
    nodes = [
      {
        role = "control-plane"
        kubeadmConfigPatches = [
          <<-EOF
          kind: InitConfiguration
          nodeRegistration:
            kubeletExtraArgs:
              node-labels: "ingress-ready=true"
          EOF
        ]
        extraPortMappings = [
          {
            containerPort = 80
            hostPort = 80
            protocol = "TCP"
          },
          {
            containerPort = 443
            hostPort = 443
            protocol = "TCP"
          }
        ]
      },
      {
        role = "worker"
      }
    ]
  })
}

# Kubernetes Namespace
resource "local_file" "k8s_namespace" {
  filename = "${path.module}/../k8s/namespace.yaml"
  content = yamlencode({
    apiVersion = "v1"
    kind = "Namespace"
    metadata = {
      name = "automation-engine"
      labels = {
        name = "automation-engine"
        managed-by = "terraform"
      }
    }
  })
}

# Output cluster info
output "registry_url" {
  value = "localhost:5000"
}

output "kind_config_path" {
  value = local_file.kind_config.filename
}

output "setup_commands" {
  value = <<-EOF
    # Create kind cluster
    kind create cluster --config=${local_file.kind_config.filename} --name=automation-engine
    
    # Connect registry to cluster network
    docker network connect kind localhost-registry || true
    
    # Update kubeconfig
    kubectl cluster-info --context kind-automation-engine
    
    # Apply namespace
    kubectl apply -f ${local_file.k8s_namespace.filename}
  EOF
}