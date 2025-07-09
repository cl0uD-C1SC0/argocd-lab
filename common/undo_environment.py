from util import run_command, change_directory, remove_directory, remove_file


def delete_terraform_environment():
    files_to_delete = [".terraform.lock.hcl", "terraform.tfstate", "terraform.tfstate.backup"]

    print(" ℹ️  Deleting Terraform Environment...")
    run_command("terraform destroy --auto-approve", shell=True) 

    for file in files_to_delete:
        remove_file(file)
    remove_directory(PATH="./terraform") 

    print(" ✅ Terraform Environment has been deleted!")


if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")