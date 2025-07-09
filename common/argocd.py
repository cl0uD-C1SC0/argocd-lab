from util import change_directory
import os

def set_git_credentials(ARGO_APPS_PATH, argocd_credentials):
    change_directory(ARGO_APPS_PATH)
    print(" ℹ️  Setting git credentials...")
    for argo_app in os.listdir():
        with open(argo_app, 'r') as file:
            content = file.read()
        
        content = content.replace("{git-username}", argocd_credentials[0])
        content = content.replace("{git-password}", argocd_credentials[1])

        with open(argo_app, 'w') as file:
            file.write(content)

    print(" ✅ Git Credentials are been configured!")

def init_argocd_configs(BASE_PATH, ARGO_APPS_PATH):
    argocd_credentials = []
    print(" ℹ️  Getting GIT Credentials...")
    with open(f'{BASE_PATH}/terraform_outputs', 'r') as file:
        credentials = file.readlines()
        git_user = credentials[0]
        git_password = credentials[1]
        argocd_credentials.append(git_user)
        argocd_credentials.append(git_password)

    set_git_credentials(ARGO_APPS_PATH, argocd_credentials)

if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")