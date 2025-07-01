from python_terraform import *
import time

tf_client = Terraform()

def apply_terraform_environment():
    print("  ℹ️  The Terraform will be create the following resources in AWS Cloud: ")
    print("   |---------------------------------------|-------------------------------------|")
    print("   |            AWS RESOURCE               |          RESOURCE NAME              |")
    print("   |---------------------------------------|-------------------------------------|")
    print("   |  AWS Virtual Private Cloud            | argocd-vpc                          |")
    print("   |  AWS Public Subnets                   | pub-argocd-1a and pub-argocd-1b     |")
    print("   |  AWS Private Subnets                  | priv-argocd-1a and priv-argocd-1b   |")
    print("   |  AWS Route Tables                     | pub-rtb-argocd and priv-rtb-argocd  |")
    print("   |  AWS Internet Gateway                 | argocd-igw                          |")
    print("   |  AWS NAT Gatewat                      | argocd-natgw                        |")
    print("   |  AWS Elastic Kubernetes Service       | argocd-poc-cluster                  |")
    print("   |  AWS Elastic Container Registry       | flask-app                           |")
    print("   |  Correctly routes in the Route tables |                                     |")
    print("   |---------------------------------------|-------------------------------------|\n")
    time.sleep(2)
    print("  ℹ️  Applying Terraform Environment ")
    print("  ℹ️  Wait a few minutes...")
    tf_client.apply()
    print("  ✅ Terraform has been applied!")
    ...

def delete_terraform_environment():
    print("  ℹ️  Deleting Terraform Environment...")
    tf_client.destroy()
    print("  ✅ Terraform Environment has been deleted!")
    ...

def start(TERRAFORM_PATH, propose):
    os.chdir(TERRAFORM_PATH)
    if propose == "apply":
        apply_terraform_environment()
        return "Terraform Environment Applied"
    delete_terraform_environment()
    return "Terraform Environment Deleted"