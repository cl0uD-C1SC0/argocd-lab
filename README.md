# ARGOCD ROLLOUTS - PROOF OF CONCEPT

Neste repositório você terá acesso a todas as ferramentas utilizadas para realizar a instalação, configuração e testes do ArgoCD Rollouts.

**Uma breve descrição a respeito:**

O ArgoCD Rollouts, ou melhor, Argo Rollouts é um controler e um conjunto de recursos customizados (Custom resources) do Kubernetes que permite a entregá progressiva de aplicações no Kubernetes.

Ele extende o recurso nativo do Kubernetes (Deployments) com um recurso avançado de Rollout, neste repositório vamos trabalhar com "três", sendo eles:

* **Canary**
* **Rollback**
* **Blue/Green**

Mais a frente, com uma leve ênfase, explicarei em resumo o que cada tipo de "entrega" faz. <br><br>

<div align="center">
    O Laboratório foi feito utilizando o AWS Sandbox da:
    <br><img src="https://img.shields.io/badge/Pluralsight-F15B2A?logo=pluralsight&logoColor=fff">
</div>

## INDEX

**PARTE 01: Introdução**
*   * [Tecnologias utilizadas](#tecnologias-utilizadas)
*   * [Organização do repositório](#organização-do-repositório)
*   * [Iniciar o Laboratorio](#como-iniciar-o-lab)

## Tecnologias utilizadas


<div align="center">
    <img src="https://img.shields.io/badge/Argo%20CD-1e0b3e?style=for-the-badge&logo=argo&logoColor=#d16044">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
    <img src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white">
    <img src="https://img.shields.io/badge/Markdown-000?style=for-the-badge&logo=markdown">
    <img src="https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
    <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
    <img src="https://img.shields.io/badge/Linux-000?style=for-the-badge&logo=linux&logoColor=FCC624">
    <img src="https://custom-icon-badges.demolab.com/badge/AWS-%23FF9900.svg?logo=aws&logoColor=white">
    <img src="https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=fff">
    <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff">
    <img src="https://img.shields.io/badge/Terraform-844FBA?logo=terraform&logoColor=fff">
    <img src="https://custom-icon-badges.demolab.com/badge/Visual%20Studio%20Code-0078d7.svg?logo=vsc&logoColor=white">

</div>


## Organização do repositório

### 📁 Ansible/playbooks

Neste diretório você encontrará scripts feitos em Ansible, esses scripts estão localizados dentro do subdiretório **playbooks**.

Abaixo, você encontrará uma breve descrição de cada um

NOME | OBJETIVO |
---| ---|
**get-argocd-credentials.yml** | Responsável por obter as credenciais do ArgoCD e salvar em um arquivo local chamado **argocd_credentials.txt**
**install-argocd.yml** | Instala o ArgoCD dentro do Cluster Kubernetes
**install-ingress-nginx.yml** | Instala o Ingress-nginx dentro do Cluster Kubernetes
**install-rollouts-cli.yml** | Instala o Argo Rollouts CLI no **WSL ou Linux**
**install-rollouts.yml** | Instala o Argo Rollouts no Cluster Kubernetes 

### 📁 ArgoCD

O Diretório do ArgoCD é responsável por conter manifestos e documentações de como realizar/simular os ambientes de **canary** e **blue-green** dentro do ArgoCD, além disso, contém instruções de como configurar **usuários**, **roles**, **adicionar clusters kubernetes** e outros.

Abaixo uma breve descrição de cada item dentro do diretório

NOME | OBJETIVO |
---| ---|
📁 blue-green | Diretório com manifestos e documentação a respeito de como realizar o **Blue-green**
📁 canary-and-rollback | Diretório com manifestos e documentação sobre o **Canary deploy & Rollback**
📁 pipeline | Diretório que contém a topologia da Pipeline utiliada pelo **GitHub Actions**
📁 projects-management | Diretório que contém a documentação sobre gerenciamento de projetos no ArgoCD
📁 user-management | Diretório que contém uma documentação a respeito do gerenciamento de usuários e permissões
📃 argocd-in.yml | Arquivo de Ingress de exemplo para expor o ArgoCD via Ingress-nginx
ℹ️ README.md | Documentação com detalhes sobre cada subdiretório dentro do diretório raiz **ArgoCD**

### 📁 Terraform

Diretório **core** (principal), contém todos os arquivos da infraestrutura, separados por módulos e totalmente customizável de acordo com suas preferências.

> OBS: O Ambiente deste laboratório será dentro da AWS apenas.

Abaixo uma breve descrição de cada item dentro do diretório

NOME | OBJETIVO |
---| ---|
📁 modules | Contém todos os módulos utiliazados pelo Terraform
📃 main.tf | Arquivo principal com as variáveis que você pode customizar de acordo com sua preferência
📃 outputs.tf | Variáveis que são mostradas após o Terraform ser aplicado
📃 providers.tf | Provedor que será utilizado, neste caso **AWS**
ℹ️ README.md | Documentação importante sobre como customizar o Terraform e outras informações

### 📁🐍 Utils

Neste diretório terá scripts em Python que será utilizado pelo script inicailizador **(init.py)**, portanto, **não realize nenhuma alteração dentro deste diretório**

Abaixo uma descrição de cada arquivo

NOME | OBJETIVO |
---| ---|
🐍 ansible.py | Script responsável por aplicar o Ansible/playbooks
🐍 terraform.py | Script responsável por aplicar o Terraform

### 📁 Docker

Contém o Dockerfile e o app, feito em Flask (Python), que será utilizado como base neste laboratório.

## Como iniciar o Lab?

O Laboratório **"roda"** interiamente dentro do ambiente **AWS** e será necessário algumas permissões listadas abaixo. 

> Não utilize a conta **ROOT** ou em **Ambientes produtivos**, não me responsabilizo por faturas ou danos causados pela execução do laboratório, **fica totalmente por sua conta e risco**!

**01 - REQUISITOS MÍNIMOS**

- Sistema operacional: Linux (Preferencialmente: Ubuntu/Debian)
- Python3.x
- AWS CLI
- AWS Configure **(Credenciais previamente configurada)**
- Ansible
- Terraform
- **AWS Account com as permissões**: <br>
    - Criar VPC com:
        - Subnet
        - Internet Gateway
        - Elastic IP
        - NAT Gateway
        - Route & Route Tables
        - Associação de Subnet
        - Gerenciamento da VPC como um todo
    - Criar um Cluster EKS & Associar um IAM user
    - Criar Node Group com instâncias EC2
    - Criar CodePipeline
    - Criar CodeBuild
    - Criar CodeCommit
    - Criar Roles no IAM para o AWS EKS
    - Criar um Elastic Container Registry (AWS ECR)

**02 - Instale as dependências**
```bash
pip install -r requirements.txt
# ou
python -m pip install requirements.txt
# ou
python3 -m pip install requirements.txt
```

**03 - INICIALIZE O SCRIPT**
```bash
python init.py
# ou
python3 init.py
```

**04 - ESCOLHA A OPÇÃO 01**
```bash
Opção 1: Configure Environment
Opção 0: Delete Environment

SELECT AN OPTION: 1
```

* Aguarde até a execução total do script, atente-se aos **outputs** (saídas).
* Exemplo de execução do script: [CLIQUE AQUI](./images/script-exec.png)

<br>

**‼️PONTOS IMPORTANTES‼️**

> OBS: Atente-se as permissões utilizadas para realizar a criação deste laboratório

> OBS2: Não interrompa a execução do Script

> OBS3: Atente-se a execução do Script, na instalação do Argo Rollouts CLI será necessário privilégios **sudo**



---
<br>

<div align="center">
    Laboratório produzido por: José Silva 🚀
    <br><br>
    <a href="https://www.linkedin.com/in/jgsiqueiraa/">
        <img src="https://img.shields.io/badge/-LinkedIn-0A66C2?logo=linkedin&logoColor=white&style=for-the-badge" />
    </a>
    <a href="https://github.com/cl0uD-C1SC0">
        <img src="https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white&style=for-the-badge" />
    </a>
</div>
