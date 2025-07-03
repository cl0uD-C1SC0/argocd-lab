import subprocess
import os
import time

def get_argocd_credentials(BASE_PATH):
    print("  ℹ️  Getting Argo credentials")
    result = subprocess.run(
    ["ansible-playbook", "get-argocd-credentials.yml"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
    )
    with open(f'{BASE_PATH}/argocd_credentials.txt', 'w') as file:
        for line in result.stdout.splitlines():
            if "ARGO" in line.replace(' ', ''):
                file.write(line.strip().replace('"', '').replace(",", "") +"\n")
    
    print("  ✅  Credentials are been saved on the following file: argocd_credentials.txt")


def apply_ansible_scripts():
    print("  ℹ️  The following scripts will be applied in the Environment: ")
    print("   |---------------------------------------|-------------------------------------|")
    print("   |           ANSIBLE SCRIPT              |            SCRIPT NAME              |")
    print("   |---------------------------------------|-------------------------------------|")
    print("   |  Install ArgoCD                       | install-argocd.yml                  |")
    print("   |  Install Argo Rollouts                | install-rollouts.yml                |")
    print("   |  Install Argo Rollouts CLI            | install-rollouts-cli.yml            |")
    print("   |  Install Ingress Nginx                | install-ingress-nginx.yml           |")
    print("   |---------------------------------------|-------------------------------------|\n")
    time.sleep(2)
    print("  ℹ️  Applying Ansible scripts")
    for script in os.listdir():
        if script.startswith("install"):
            subprocess.run(
                ["ansible-playbook", f"{script}"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            print(f"  ✅ Script: {script} has been applied!")
    print(f"  ✅ All scripts has been applied in the Environment!")
    

def start(BASE_PATH, ANSIBLE_PATH):
    os.chdir(ANSIBLE_PATH)
    apply_ansible_scripts()
    get_argocd_credentials(BASE_PATH)

if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")