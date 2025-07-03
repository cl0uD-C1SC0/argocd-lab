import time
import os
import shutil
import subprocess

def init_terraform_environment():
    print("  ℹ️  Initializying Terraform Environment ")
    subprocess.run(
        ["terraform", "init"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print("  ✅ Terraform has been initialized")

    ...

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
    subprocess.run(
        ["terraform", "apply", "--auto-approve"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print("  ✅ Terraform has been applied!")

def delete_terraform_environment():
    files_to_delete = [".terraform", ".terraform.lock.hcl", "terraform.tfstate", "terraform.tfstate.backup"]

    print("  ℹ️  Deleting Terraform Environment...")
    subprocess.run(
        ["terraform", "destroy", "--auto-approve"]       
    )
    for file in files_to_delete:
        if file == ".terraform":
            shutil.rmtree(file)
        else:
            os.remove(file)
    print("  ✅ Terraform Environment has been deleted!")

def start(TERRAFORM_PATH, propose):
    os.chdir(TERRAFORM_PATH)
    if propose == "apply":
        init_terraform_environment()
        apply_terraform_environment()
        return "Terraform Environment Applied"
    delete_terraform_environment()
    return "Terraform Environment Deleted"