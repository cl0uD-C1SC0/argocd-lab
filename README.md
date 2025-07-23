<div align="center"><img src="./images/sandbox-logo.png" width=250px></div><br><br>

# ArgoCD and Argo Rollouts - SandBox Environment

Bem-vindo ao ArgoCD & Argo Rollouts Lab!

Um laboratório que trará documentações completas a respeito do uso do ArgoCD e principalmente, o carro chefe, o Argo Rollouts!

Está 100% automatizado e roda dentro do ambiente da AWS! É importante ressaltar que, o repositório inteiro conta com documentações em PT-BR feitas para que você aprenda de uma vez por todas o uso dessas duas ferramentas extremamente úteis para um ambiente totalmente DevOps.

Conta com recursos e tecnologias bem interessantes, vale dar uma olhada nessa documentação depois: [ArgoCD - Introdução](./ArgoCD/), mas só depois em!

Qualquer problema ou dúvidas na execução do laboratório, fico a disposição via LinkedIn (Link no final do README.md)!

Bons estudos!

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
📁 Ansible | Scripts, localizado dentro do diretório playbooks/. São utilizados para instalar e configurar o laboratório | [Documentação Ansible](./Ansible/)
📁 App | Código em Flask utilizado como base | [Documentação do APP](./app/)
📁 ArgoCD | Documentações do ArgoCD como: Canary e Blue/Green deployments, usuários e roles | [Documentação ArgoCD](./ArgoCD/)
📁 Kubernetes | Contém todos os manifestos utilizados e uma breve documentação sobre | [Documentação k8s](./Kubernetes/)
📁 Terraform | Contém módulos do Terraform e toda infraestrutura baseada em IaC | [Documentação do Terraform](./Terraform/)
📁🐍 Common | Contém todos os códigos/scripts em Python utilizado para providênciar de forma automática o Laboratório | [Documentação dos scripts Python](./common/)
📁🔑 security | Permissões que você precisa ter na sua conta AWS | [Documentação das permissões](./security/) 
📁 images | Imagens utilizadas pelo repositório | ❌ 


## Como iniciar o Lab?

⌚️ **Tempo de execução para criar: 13 minutos**

> ⚠️ O Repositório é totalmente inicializado dentro da sua conta AWS. Portanto, tome cuidado. Utilize as permissões definidas logo mais abaixo para a prática **Least Privilege** 

> ⚠️ Não é recomendado utilizar contas da AWS produtivas neste ambiente. 

**REQUISITOS MÍNIMOS**

- Sistema operacional: Linux (Preferencialmente: Ubuntu/Debian)
- Python3.x
- AWS CLI
- AWS Configure **(Credenciais previamente configurada)**
- Ansible
- Terraform
- **Permissões**: [CLIQUE AQUI PARA VISUALIZAR AS PERMISSÕES NECESSÁRIAS](./security/)

> Utilize a permissão: security/fully_compressed-policy.json em seu ambiente para construir algo mais Least Privilege e controlado no quesito segurança

**01 - Configure o usuárino no arquivo terraform**

> Troque o valor de YOUR_AWS_USER pelo o seu Usuario AWS utilizado durante o laboratorio

```terraform
module "codecommit" {
    source = "./modules/CodeCommit"

    codecommit-credentials-user = "YOUR_AWS_USER" # Default: argocd_user

}
```
[CLIQUE AQUI - ARQUIVO PARA MODIFICAR](./Terraform/main.tf)

**02 - Instale as dependências**
```bash
python -m pip install -r requirements.txt
ansible-galaxy collection install -r requirements.yml
```

**03 - INICIALIZE O SCRIPT**
```bash
python init.py
```

**04 - ESCOLHA A OPÇÃO 01**
```bash
Opção 1: Configure Environment
Opção 0: Delete Environment

SELECT AN OPTION: 1
```

* Aguarde até a execução total do script, atente-se aos **outputs** (saídas).

**05 - Após a criação do ambiente ser finalizada, automaticamente o context do kubectl é configurado**
```bash
kubectl config get-contexts
```

**06 - Após a execução do script, os seguintes outputs serão gerados**

- OUTPUT 1: **argocd_credentials.txt** 
    - Contém as credenciais de acesso ao ArgoCD + URL

- OUTPUT 2: **terraform_outputs**
    - Contém as credenciais do AWS CodeCommit

<br>


<div align="center">

🚨🚨🚨

████████████████████████████████████████████████████████ ██ ██ ██ 🚨
<li>Atente-se as permissões utilizadas para a realização do laboratório</li> 
<li>Atente-se na etapa manual do script, requisitará acesso elevado no Linux!</li>
<li>Script verboso, significa que qualquer erro será mostrado no terminal, portanto, não o interrompa</li> <br>

🚨 ██ ██ ██ ████████████████████████████████████████████████████████

<div>

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
