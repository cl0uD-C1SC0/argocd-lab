import os
import sys
import time
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), 'common'))
from common import terraform as terraform_script
from common import ansible as ansible_script
from common import codecommit_push as code_push
from common import argocd
from common import util

# DON'T CHANGE THESE VARIABLES

start_time = datetime.datetime.now()

BASE_PATH = os.getcwd()
TERRAFORM_PATH  = f'{BASE_PATH}/Terraform'
ANSIBLE_PATH    = f'{BASE_PATH}/Ansible/playbooks'
APP_PATH        = f'{BASE_PATH}/Docker/'
ARGO_APPS_PATH  = f'{BASE_PATH}/Kubernetes/argo-apps'

general_options = {
    'Configure Environment': '1',
    'Delete Environment': '0',
}

def calc_execution_time():
    end_time = datetime.datetime.now()
    execution_time = (end_time - start_time) / 60
    print(f"\n ✅ Script takes {execution_time.total_seconds()} minutes to Done")

def init_time(message):
    timer_list = ["1️⃣", "2️⃣", "3️⃣"]
    print(" ℹ️  May this script need some manual interactions, pay attention please!")
    print(" ⚠️  Please, don't stop the script execution!\n")
    for i in timer_list:
        print(f" ℹ️  {message} the environment in {i}")
        time.sleep(1)

def set_aws_cluster():
    print(" ℹ️  Updating the Kubeconfig")
    util.run_command(COMMAND="aws eks update-kubeconfig --name argocd-poc-cluster --region us-east-1", shell=True)
    print(" ✅ Kubeconfig has been Updated!")

def start_execution(user_choice, BASE_PATH, TERRAFORM_PATH, ANSIBLE_PATH, ARGO_APPS_PATH):     
    if user_choice == 1:
        init_time(message="Initializing")
        
        print("\n 🟢 INITIALIZING THE ENVINRONMENT 🟢\n")
        print(" ℹ️  Configuring the environment...")

        terraform_script.init_terraform_configs(BASE_PATH, TERRAFORM_PATH)
        set_aws_cluster()
        argocd.init_argocd_configs(BASE_PATH, ARGO_APPS_PATH)
        ansible_script.init_ansible_configs(BASE_PATH, ANSIBLE_PATH)
        code_push.init_codecommit_configs(BASE_PATH)
        ansible_script.apply_argocd_apps()

        print(f" ✅ Environment has been created")
        calc_execution_time()
        return "Environment created"
    elif user_choice == 0:
        init_time(message="Deleting")
        calc_execution_time()
        return "Environment Deleted"
    print(" ❌  Invalid Option, try again...")
    return "Invalid Option, try again"

if __name__ == '__main__':
    for option, value in general_options.items():
        print(f"Opção {value}: {option}" )

    user_choice = int(input("\nSELECT AN OPTION: "))
    start_execution(user_choice, BASE_PATH, TERRAFORM_PATH, ANSIBLE_PATH, APP_PATH, ARGO_APPS_PATH)
