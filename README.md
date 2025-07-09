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
*   * [Por que o ArgoCD?](#por-que-o-argocd)
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

## Por que o ArgoCD?

O ArgoCD é uma ferramenta amplamente utilizada por diversas equipes de DevOps ao redor do mundo, e é claro, é uma ferramenta aprovada pela CNCF (Graduated) e mantida pela **The Linux Foundation**.

É uma ferramenta que permite a entrega contínua (CD), declarativa e open-source, baseada totalmente no GitOps para o Kubernetes. Permite automatizar a implementação de aplicações, sincronizando o estado desejado e definido em um repositório Git. Em outras palavras, o que estiver no repositório Git, o ArgoCD faz questão de garantir que ele seja aplicado dentro do Kubernetes (na questão de manifestos k8s).

Alguns pontos interessantes:

* Estado desejado: O Estado desejado de sua aplicação é definido em arquivos de config (Yaml, Kustomize, Helm ou outros) e são armazeandos em Git
* Monitoramento Contínuo: O ArgoCD monitora continuamente o seu cluster Kubernetes e o repositório Git
* Comparação e Sincronização: Compara o estado atual do seu cluster com o estado desejado do Git e identifica desvios
* Reconciliação: Se houver desvios, o ArgoCD pode automaticamente reconciliar (sincronizar) o estado do seu cluster com o estado desejado ou, opcionalmente, permitir que um operador faça isso manualmente 
* Git como fonte de verdade: O Git se torna a única fonte confiável para o estado da sua aplicação, facilitando o versionamento, auditoria e rollback de implantações. 

Abaixo uma imagem que descreve, em resumo, o funcionamento do ArgoCD: <br>

<img src="./images/ArgoCD-topology.png">

<br><br>

Mais adiante eu o convido a explorar mais a respeito do repositorio e por fim iniciar esse laboratório.

Qualquer problema na execução ou falha do script, peço que me contate nas redes que deixarei no fim deste **README.md**, desejo um bom resto de dia e bons estudos à você! 👍

## Organização do repositório

| DIRETÓRIO | OBJETIVO | DOCUMENTAÇÃO
---| ---| ---|
📁 Ansible/playbooks | Scripts que são utilizados para instalar e configurar os componentes da infraestrutura | [Documentação Ansible scripts](./Ansible/)
📁 App | Código em Flask utilizado como base | [Documentação do APP](./app/)
📁 ArgoCD | Documentações do ArgoCD como: Canary e Blue/Green deployments, usuários e roles | [Documentação ArgoCD](./ArgoCD/)
📁 Kubernetes | Contém todos os manifestos utilizados e uma breve documentação sobre | [Documentação k8s](./Kubernetes/)
📁 Terraform | Contém módulos do Terraform e toda infraestrutura baseada em IaC | [Documentação do Terraform](./Terraform/)
📁🐍 Common | Contém todos os códigos/scripts em Python utilizado para providênciar de forma automática o Laboratório | [Documentação dos scripts Python](./common/)
📁 images | Imagens utilizadas pelo repositório | ❌ 


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
