import subprocess
import os
import time
from util import run_command

def ansible_resources_to_apply_info():
    resources = [
        ("Install ArgoCD", "install-argocd.yml"),
        ("Install Argo Rollouts", "install-rollouts.yml"),
        ("Install Argo Rollouts CLI", "get-rollouts-cli.yml"),
        ("Install Ingress Nginx", "install-ingress-nginx.yml"),
        ("Get ArgoCD Credentials", "get-argocd-credentials.yml"),
        ("Apply ArgoCD APPs", "apply-argo-apps.yml")
    ]
    print(" ℹ️  The following scripts will be applied in the Environment: ")
    print("   |---------------------------------------|-------------------------------------|")
    print("   | {:<37} | {:<35} |".format("ANSIBLE SCRIPT", "SCRIPT NAME"))
    print("   |---------------------------------------|-------------------------------------|")
    for res, name in resources:
        print("   | {:<37} | {:<35} |".format(res, name))
    print("   |---------------------------------------|-------------------------------------|\n")

def install_argo_rollouts_cli():
    print(" ℹ️  Installing the Argo Rollouts CLI")
    run_command(COMMAND="ansible-playbook get-rollouts-cli.yml", shell=True)
    print(" ✅ Argo Rollouts CLI has been installed on system!")

def apply_argocd_apps():
    print(" ℹ️ Applying ArgoCD APPs")
    run_command(COMMAND="ansible-playbook apply-argo-apps.yml", shell=True)
    print(" ✅ ArgoCD APPs applyed!")

def get_argocd_credentials(BASE_PATH):
    print(" ℹ️  Getting Argo credentials")
    result = run_command(COMMAND="ansible-playbook get-argocd-credentials.yml", text=True, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    with open(f'{BASE_PATH}/argocd_credentials.txt', 'w') as file:
        for line in result.splitlines():
            if "ARGO" in line.replace(' ', ''):
                file.write(line.strip().replace('"', '').replace(",", "") +"\n")
    
    print(" ✅ Credentials are been saved on the following file: argocd_credentials.txt")


def apply_install_ansible_scripts():
    ansible_resources_to_apply_info()
    time.sleep(2)
    print(" ℹ️  Applying 'Install' Ansible scripts")
    for script in os.listdir():
        if script.startswith("install"):
            print(f" ℹ️  Applying the following script {script}")
            run_command(COMMAND=f"ansible-playbook {script}", shell=True)
            print(f" ✅ Script: {script} has been applied!")
    print(f" ✅ All scripts has been applied in the Environment!")
    

def init_ansible_configs(BASE_PATH, ANSIBLE_PATH):
    os.chdir(ANSIBLE_PATH)
    apply_install_ansible_scripts()
    get_argocd_credentials(BASE_PATH)

    print(" ℹ️  Default is: No ")
    user_choice = "NO"
    user_choice = input(" ⁉️  Do you want to install Argo Rollouts CLI (Yes/Y|No/N)?: ").upper()
    if user_choice == 'YES' or user_choice == 'Y' :
        install_argo_rollouts_cli()
        return "Ok"
    return "Ok" 

if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")