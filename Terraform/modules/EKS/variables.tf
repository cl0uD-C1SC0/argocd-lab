variable "eks_cluster-name" {
  description = "EKS Cluster Name"
  type = string
  default = "tf-eks-cluster"
}

variable "eks_cluster_ndg-name" {
  description = "EKS Nodegroup Name"
  type = string
  default = "tf-ndg"
}

variable "eks_cluster_iam-name" {
  description = "EKS Cluster IAM AmazonEKSClusterPolicy"
  type = string
  default = "tf-AmazonEKSClusterPolicy"
}

variable "vpc_id" {}
variable "pubsubnet" {
  type = list(string)
}