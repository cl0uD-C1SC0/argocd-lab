module "vpc" {
    source = "./modules/VPC"

    # Default names use "tf-<resource_name>" as prefix

    vpc_name = "argocd-vpc" # Default = tf-vpc
    vpc_cidr = "10.0.0.0/16" # Default = 192.168.0.0/16
    vpc_internetgateway_name = "argocd-igw"   # Default = tf-igw 
    vpc_natgateway_name      = "argocd-natgw" # Default = tf-natgw

    # PUBSUBNET 1
    vpc_pubsubnet_1-az   = "us-east-1a"    # Default = us-east-1a
    vpc_pubsubnet_1-cidr = "10.0.0.0/24"   # Default = 192.168.0.0/24
    vpc_pubsubnet_1-name = "pub-argocd-1a" # Default = tf-pub1a

    # PUBSUBNET 2
    vpc_pubsubnet_2-az   = "us-east-1b"    # Default = us-east-1b
    vpc_pubsubnet_2-cidr = "10.0.1.0/24"   # Default = 192.168.1.0/24
    vpc_pubsubnet_2-name = "pub-argocd-1b" # Default = tf-pub2b

    # PRIVSUBNET 1
    vpc_privsubnet_1-az   = "us-east-1a"     # Default = us-east-1a
    vpc_privsubnet_1-cidr = "10.0.2.0/24"    # Default = 192.168.2.0/24
    vpc_privsubnet_1-name = "priv-argocd-1a" # Default = tf-priv1a

    # PRIVSUBNET 2
    vpc_privsubnet_2-az   = "us-east-1b"     # Default = us-east-1b
    vpc_privsubnet_2-cidr = "10.0.4.0/24"    # Default = 192.168.3.0/24
    vpc_privsubnet_2-name = "priv-argocd-1b" # Default = tf-priv2b

    # Elastic IP
    elastic_ip-name = "argocd-eip-natgw" # Default = eip-argocd

    # RTB
    rtb_pub-name  = "pub-rtb-argocd"  # Default = pub-rtb-tf
    rtb_priv-name = "priv-rtb-argocd" # Default = priv-rtb-tf
}

module "eks" {
    source = "./modules/EKS"

    vpc_id    = module.vpc.vpc_id
    pubsubnet = module.vpc.public_subnets
    eks_cluster-name    = "argocd-poc-cluster"             # Default = tf-eks-cluster
    eks_cluster_iam-name = "AmazonEKSClusterPolicy-argocd" # Default = tf-AmazonEKSClusterPolicy
    eks_cluster_ndg-name = "argocd-ndg"                    # Default = tf-ndg
}

module "ecr" {
    source = "./modules/ECR"

    ecr_argocd_repo-name = "flask-app"
}

module "codecommit" {
    source = "./modules/CodeCommit"

    codecommit-credentials-user = "cloud_user"

}