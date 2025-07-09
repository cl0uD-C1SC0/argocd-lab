# 📂 Ansible/playbooks

ORGANIZAÇÃO DOS SCRIPTS EM: [**playbooks/**](./playbooks/)

NOME | OBJETIVO |
---| ---|
**get-argocd-credentials.yml** | Responsável por obter as credenciais do ArgoCD e salvar em um arquivo local chamado **argocd_credentials.txt**
**install-argocd.yml** | Instala o ArgoCD dentro do Cluster Kubernetes
**install-ingress-nginx.yml** | Instala o Ingress-nginx dentro do Cluster Kubernetes
**get-rollouts-cli.yml** | Instala o Argo Rollouts CLI no **WSL ou Linux**
**install-rollouts.yml** | Instala o Argo Rollouts no Cluster Kubernetes 
**apply-argo-apps.yml** | Aplica/Cria os APPS dentro do ArgoCD