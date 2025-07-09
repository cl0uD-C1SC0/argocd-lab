<img src="../images/banner-argocd.png"> <br><br>



**ÍNDICE**

* [1 - Estrutura do diretório](#estrutura-do-diretório)
* [2 - Comandos gerais no ArgoCD CLI](#comandos-gerais-argocd-cli)
* [3 - O que é Canary Deployment](./canary/README.md)
* [4 - O que é Blue/Green Deployment](./blue-green/README.md)
* [5 - Como criar e gerenciar usuários no ArgoCD](./user-management/)
* [6 - Sobre Projects no ArgoCD](./projects-management/)

## Estrutura do diretório:

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

## Comandos gerais ArgoCD CLI:

### Login no ArgoCD CLI:

```bash
ARGOCDURL=$(kubectl get svc argocd-server -n argocd -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
argocd login $ARGOCDURL
```

### Add context/cluster no ArgoCD

> 01 - Renomeie o contexto existente
```bash
kubectl config get-contexts
kubectl config rename-context <contexto_atual> <nome_novo>
```

> 02 - Adicione um novo contexto/cluster no ArgoCD em um projeto especifico
```bash
argocd cluster add <CONTEXT_NAME> --project <PROJECT_NAME>
```

