aws_region     = "us-west-2"
environment    = "dev"
cluster_name   = "automation-engine-cluster"
cluster_version = "1.28"

node_group_instance_types = ["t3.medium"]
node_group_desired_size   = 2
node_group_max_size       = 4
node_group_min_size       = 1