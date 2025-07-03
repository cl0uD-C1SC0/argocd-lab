import os
import sys
import subprocess
import time
import datetime

start_time = datetime.datetime.now()

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
from utils import terraform as tf_script
from utils import docker as docker_script
from utils import ansible as ansible_script

def terraform_func(TERRAFORM_PATH, propose):
    tf_script.start(TERRAFORM_PATH, propose)
    ...

def set_aws_cluster():
    print("  ℹ️  Updating the Kubeconfig")
    subprocess.run(
        ["aws", "eks", "update-kubeconfig", "--name", "argocd-poc-cluster", "--region", "us-east-1"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    print("  ✅ Kubeconfig has been Updated!")

def apply_ansible(BASE_PATH, ANSIBLE_PATH):
    ansible_script.start(BASE_PATH, ANSIBLE_PATH)

def docker_build(DOCKER_PATH):
    ...

def delete_environment(TERRAFORM_PATH, propose):
    print("  ℹ️  Cleaning the environment...")
    print("  ⚠️  Please, don't stop the script execution!\n\n")

    terraform_func(TERRAFORM_PATH, propose)
    end_time = datetime.datetime.now()
    execution_time = end_time - start_time
    print(f"\n  ✅  Environment takes {execution_time.total_seconds()} secods to delete")

def configure_environment(BASE_PATH, TERRAFORM_PATH, ANSIBLE_PATH, DOCKER_PATH, propose):   
    print("  ℹ️  Configuring the environment...")
    print("  ⚠️  Please, don't stop the script execution!\n\n")
    time.sleep(2)

    terraform_func(TERRAFORM_PATH, propose)
    set_aws_cluster()
    apply_ansible(BASE_PATH, ANSIBLE_PATH)
    #docker_build(DOCKER_PATH)

    end_time = datetime.datetime.now()
    execution_time = end_time - start_time
    print(f"\n  ✅  Environment takes {execution_time.total_seconds()} secods to create")

if __name__ == '__main__':
    BASE_PATH = os.getcwd()
    TERRAFORM_PATH  = f'{BASE_PATH}/Terraform'
    ANSIBLE_PATH    = f'{BASE_PATH}/Ansible/playbooks'
    DOCKER_PATH     = f'{BASE_PATH}/Docker'

    general_options = {
        'Configure Environment': '1',
        'Delete Environment': '0',
    }

    for option, value in general_options.items():
        print(f"Opção {value}: {option}" )

    user_choice = int(input("\nSELECT AN OPTION: "))
    if user_choice == 1:
        configure_environment(BASE_PATH, TERRAFORM_PATH, ANSIBLE_PATH, DOCKER_PATH, propose="apply")
        print(f"  ✅  Environment has been created")
    
    elif user_choice == 0:
        delete_environment(TERRAFORM_PATH, propose="delete")
        print(f"  ✅ Environment has been deleted")

    else:
        print("  ❌  Invalid Option, try again...")
