# 📁🐍 Common

Neste diretório terá scripts em Python que será utilizado pelo script inicailizador **(init.py)**, portanto, **não realize nenhuma alteração dentro deste diretório**

Abaixo uma descrição de cada arquivo

NOME | OBJETIVO |
---| ---|
🐍 ansible.py | Script responsável por aplicar o Ansible/playbooks
🐍 terraform.py | Script responsável por aplicar o Terraform
🐍 undo_environment.py | Script responsável por deletar o ambiente
🐍 check_configs.py | Script responsável por validar os requisitos mínimos
🐍 codecommit_push.py | Script responsável por enviar os arquivos ao AWS CodeCommit
🐍 util.py | Script geral com funções utilizadas por outros scripts
🐍 argocd.py | Script que configura os repositórios/credenciais para a plataforma do ArgoCD

> OBS: ⚠️⚠️ Qualquer alteração poderá comprometer o Script como um todo, ocasionando em falhas não esperadas. ⚠️⚠️