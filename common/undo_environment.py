from util import run_command, change_directory, remove_directory, remove_file
import os

def delete_tf_files(BASE_PATH):
    change_directory(f"{BASE_PATH}/Terraform")
    print(" ℹ️  Removing Terraform Files...")
    files_to_delete = [".terraform.lock.hcl", "terraform.tfstate", "terraform.tfstate.backup"]
    
    for file in files_to_delete:
        remove_file(file)
    remove_directory(PATH="./.terraform")
    print(" ✅ Terraform files has been removed!") 

def delete_output_files(BASE_PATH):
    change_directory(BASE_PATH)
    files_to_delete = ["argocd_credentials.txt", "terraform_outputs"]
    for file in files_to_delete:
        remove_file(f"./{file}")

def destroy_terraform_env():
    print(" ℹ️  Deleting Terraform Environment...")
    run_command("terraform destroy --auto-approve", shell=True) 
    print(" ✅ Terraform Environment has been deleted!")

def init_delete_environment(BASE_PATH):
    destroy_terraform_env()
    delete_output_files(BASE_PATH)
    delete_tf_files(BASE_PATH)

if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")