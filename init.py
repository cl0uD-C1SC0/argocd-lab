import os
import sys
import subprocess
import boto3
import time

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
from utils import terraform as tf_script
from utils import docker as docker_script
from utils import ansible as ansible_script

def set_aws_credentials():
    print("  ℹ️  Define your AWS Credentials")
    ACCESS_KEY = input("ACCESS_KEY: ")
    SECRET_KEY = input("SECRET_KEY: ")

    client = boto3.client(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
    )

    print("  ✅  Credentials defined!")
    return "Ok"
    ...

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
    ...

def docker_build(DOCKER_PATH):
    ...

def configure_environment():
    BASE_PATH = os.getcwd()
    TERRAFORM_PATH  = f'{BASE_PATH}/Terraform'
    ANSIBLE_PATH    = f'{BASE_PATH}/Ansible/playbooks'
    DOCKER_PATH     = f'{BASE_PATH}/Docker'

   
    print("  ℹ️  Configuring the environment...")
    print("  ⚠️  Please, don't stop the script execution!\n\n")
    time.sleep(4)
    set_aws_credentials()
    terraform_func(TERRAFORM_PATH, propose="apply")
    set_aws_cluster()
    apply_ansible(BASE_PATH, ANSIBLE_PATH)
    #docker_build(DOCKER_PATH)

if __name__ == '__main__':
    general_options = {
        'Configure Environment': '1',
        'Delete Environment': '0',
    }

    for option, value in general_options.items():
        print(f"Opção {value}: {option}" )

    user_choice = int(input("\nSELECT AN OPTION: "))
    if user_choice == 1:
        configure_environment()
    
