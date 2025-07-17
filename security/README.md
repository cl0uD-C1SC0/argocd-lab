# Tabela de permissões:


## AWS CodeCommit
PERMISSÃO | MOTIVO
---| ---|
codecommit:CreateRepository     | Criar Repositório
codecommit:CreateBranch         | Criar Branch
codecommit:CreateCommit         | Criar Commit
codecommit:DeleteRepository     | Deletar Repositório
codecommit:DeleteFile           | Deletar um arquivo
codecommit:DeleteBranch         | Deletar uma branch
codecommit:GitPull              | GitPull via CLI
codecommit:GetFile              | Get em arquivos do repositório
codecommit:GetCommit            | Get em um commit
codecommit:GetCommitHistory     | Get no histórico de commits
codecommit:GetRepository        | Get um repositório específico
codecommit:GetBranch            | Get em uma branch
codecommit:GitPush              | Efetuar GitPush
codecommit:ListFileCommitHistory| Listar histórico de commit de um arquivo
codecommit:ListBranches         | Listar Branches
codecommit:ListTagsforResource  | Listar as Tags
codecommit:ListRepositories     | Listar os repositórios
codecommit:PutFile              | Colocar/enviar commits
codecommit:TagResource          | Colocar Tag no CodeCommit

## AWS Elastic Container Registry - ECR
PERMISSÃO | MOTIVO
---| ---|
ecr:BatchDeleteImage        | Permite deletar diversas imagens de uma vez
ecr:CreateRepository        | Permite criar um repositório
ecr:DescribeRepositories    | Permite descrever os repositórios
ecr:DescribeRegistry        | Permite descrever um registry específico
ecr:DeleteRepository        | Permite deletar o repositório 
ecr:DescribeImages          | Permite descrever imagens
ecr:GetAuthorizationToken   | Permite pegar o Token de Autorização
ecr:GetDownloadUrlForLayer  | Permite obter a URL de uma camada específica da imagem
ecr:ListTagsForResource     | Permite listar as tags de recurso
ecr:ListImages              | Permite listar as imagens
ecr:PutImage                | Permite colocar uma imagem
ecr:TagResource             | Permite colocar tag no ECR

## AWS Elastic Kubernetes Service - EKS
PERMISSÃO | MOTIVO
---| ---|
eks:AssociateAccessPolicy           | Permite Colocar/associar politica
eks:CreateCluster                   | Criar o Cluster Kubernetes
eks:CreateAddon                     | Permite Adicionar Addons
eks:CreateAccessEntry"              | Permite Criar um Access Entry
eks:CreateNodegroup                 | Permite Criar NodeGroups
eks:DescribeNodegroup               | Permite Descrever os NodeGroups
eks:DeleteAccessEntry               | Permite Deletar um Access Entry
eks:DeleteCluster                   | Permite Deletar o Cluster Kubernetes
eks:DeleteAddon                     | Permite Deletar um Addon
eks:DeleteNodegroup                 | Permite Deletar o NodeGroup
eks:DescribeCluster                 | Permite Descrever o Cluster
eks:DescribeAccessEntry             | Permite Descrever os Access Entry
eks:DescribeAddon                   | Permite Descrever os Addons
eks:DisassociateAccessPolicy        | Permite Desassociar as políticas     
eks:ListAssociatedAccessPolicies    | Permite Listar políticas associadas       
eks:TagResource                     | Permite Colocar Tag no EKS

## AWS Identity and Access Management - IAM
PERMISSÃO | MOTIVO
---| ---|
iam:AttachRolePolicy                | Permite atribuir uma Role em uma Policy
iam:CreateRole                      | Permite Criar uma Role
iam:CreateServiceSpecificCredential | Permite Criar uma credencial para um serviço específico (AWS CodeCommit)
iam:DetachRolePolicy                | Permite Desassociar uma role
iam:DeleteRole"                     | Permite Deletar uma Role
iam:DeleteServiceSpecificCredential | Permite Deletar uma credencial específica
iam:GetRole                         | Permite puxar informações de uma Role
iam:ListInstanceProfilesForRole     | Listar um instance Profile de uma role
iam:ListAttachedRolePolicies        | Listar roles associadas 
iam:ListRolePolicies                | Listar Role Policies
iam:ListServiceSpecificCredentials  | Permite Listar uma credencial específica

## AWS Virtual Private Cloud/Elastic Compute Cloud - VPC/EC2
PERMISSÃO | MOTIVO
---| ---|
ec2:AllocateAddress             | Alocar um endereço
ec2:AssociateRouteTable         | Associar uma Rota na RouteTable
ec2:AttachInternetGateway       | Atribuir um Internet Gateway
ec2:CreateNatGateway            | Criar um Nat Gateway
ec2:CreateVpc                   | Criar uma VPC
ec2:CreateTags                  | Criar Tags
ec2:CreateRouteTable            | Criar uma Route Table
ec2:CreateSubnet                | Criar uma Subnet
ec2:CreateRoute                 | Criar uma Rota
ec2:CreateInternetGateway       | Criar um Internet Gateway
ec2:DescribeSubnets             | Descrever Subnets
ec2:DeleteNatGateway            | Deletar um Nat Gateway
ec2:DescribeVpcs                | Descrever VPCs
ec2:DeleteVpc                   | Deletar uma VPC
ec2:DetachInternetGateway       | Desassociar um Internet Gateway
ec2:DescribeNatGateways         | Descrever um Nat Gateway
ec2:DisassociateRouteTable      | Desassociar uma Route Table
ec2:DeleteInternetGateway       | Deletar um Internet Gateway
ec2:DescribeRouteTables         | Descrever Route Tables
ec2:DeleteRoute                 | Deletar uma Rota
ec2:DescribeInternetGateways    | Descrever Internet Gateways
ec2:DescribeNetworkInterfaces   | Descrever Interfaces de rede
ec2:DescribeVpcAttribute        | Descrever atributos da VPC
ec2:DeleteRouteTable            | Deletar uma Route Table
ec2:DescribeAddressesAttribute  | Descrever atributos de um endereço
ec2:DisassociateAddress         | Desassociar um endereço
ec2:DeleteSubnet                | Deletar uma Subnet
ec2:DescribeAddresses           | Descrever um Endereço
ec2:ModifySubnetAttribute       | Modificar o atributo de uma Subnet
ec2:ReleaseAddress              | Liberar um Endereço IP