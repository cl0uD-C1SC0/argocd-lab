resource "aws_eks_cluster" "eks-argocd" {
  depends_on = [aws_iam_role_policy_attachment.cluster_AmazonEKSClusterPolicy]

  name = var.eks_cluster-name

  access_config {
    authentication_mode = "API_AND_CONFIG_MAP"
  }

  role_arn = aws_iam_role.eks-assume-role.arn
  version  = "1.31"

  vpc_config {
    subnet_ids = var.pubsubnet
    endpoint_public_access = true
  }
}

resource "aws_eks_node_group" "eks-ndg-argocd" {
  depends_on = [ aws_eks_cluster.eks-argocd, aws_iam_role_policy_attachment.argocd-AmazonEC2ContainerRegistryReadOnly, aws_iam_role_policy_attachment.argocd-AmazonEKS_CNI_Policy, aws_iam_role_policy_attachment.argocd-AmazonEKSWorkerNodePolicy ]

  cluster_name      = aws_eks_cluster.eks-argocd.name
  node_group_name   = var.eks_cluster_ndg-name
  node_role_arn     = aws_iam_role.eks-argocd-ndg-role.arn

  scaling_config {
    desired_size = 1
    max_size = 2
    min_size = 1    
  }
  
  update_config {
    max_unavailable = 1
  }

  subnet_ids = var.pubsubnet
}
