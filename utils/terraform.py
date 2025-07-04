import time
from util import run_command, remove_file, remove_directory, change_directory

def init_terraform_environment():
    print(" ℹ️  Initializying Terraform Environment ")
    run_command(COMMAND="terraform init")
    print(" ✅ Terraform has been initialized")

def apply_terraform_environment():
    print(" ℹ️  The Terraform will be create the following resources in AWS Cloud: ")
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
    print(" ℹ️  Applying Terraform Environment ")
    print(" ℹ️  Wait a few minutes...")
    run_command(COMMAND="terraform apply --auto-approve")
    print(" ✅ Terraform has been applied!")

def delete_terraform_environment():
    files_to_delete = [".terraform.lock.hcl", "terraform.tfstate", "terraform.tfstate.backup"]

    print(" ℹ️  Deleting Terraform Environment...")
    run_command("terraform destroy --auto-approve") 

    for file in files_to_delete:
        remove_file(file)
    remove_directory(PATH="./terraform") 

    print(" ✅ Terraform Environment has been deleted!")

def start(TERRAFORM_PATH, propose):
    change_directory(TERRAFORM_PATH)
    if propose == "apply":
        init_terraform_environment()
        apply_terraform_environment()
        return "Terraform Environment Applied"
    delete_terraform_environment()
    return "Terraform Environment Deleted"