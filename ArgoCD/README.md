<img src="../images/banner-argocd.png"> <br><br>



**ÍNDICE**

* [1 - Estrutura do diretório](#estrutura-do-diretório)
* [2 - O que é Argo Rollouts?](#o-que-é-argo-rollouts)
* [2 - Comandos gerais no ArgoCD CLI](#comandos-gerais-argocd-cli)
* [3 - O que é Canary Deployment](./canary/README.md)
* [4 - O que é Blue/Green Deployment](./blue-green/README.md)
* [5 - Como criar e gerenciar usuários no ArgoCD](./user-management/)
* [6 - Sobre Projects no ArgoCD](./projects-management/)

## Estrutura do diretório:

O Diretório do ArgoCD é responsável por conter manifestos e documentações de como realizar/simular os ambientes de **canary** e **blue-green** dentro do ArgoCD, além disso, contém instruções de como configurar **usuários**, **roles**, **adicionar clusters kubernetes** e outros.

Abaixo uma breve descrição de cada item dentro do diretório

NOME | OBJETIVO | DOCUMENTAÇÃO
---| ---|
📁 blue-green | Diretório com documentação a respeito de como realizar o **Blue-green** | [Documentação BlueGreen](./blue-green/README.md)
📁 canary-and-rollback | Diretório documentação sobre o **Canary deploy & Rollback** | [Documentação Canary](./canary/README.md)
📁 projects-management | Diretório que contém a documentação sobre gerenciamento de projetos no ArgoCD | [Documentação sobre Projects](./projects-management/README.md)
📁 user-management | Diretório que contém uma documentação a respeito do gerenciamento de usuários e permissões | [Documentação sobre Users](./user-management/README.md)
📃 argocd-in.yml | Arquivo de Ingress de exemplo para expor o ArgoCD via Ingress-nginx | ❌
ℹ️ README.md | Documentação com detalhes sobre cada subdiretório dentro do diretório raiz **ArgoCD** | ❌

## O que é Argo Rollouts?

Argo Rollouts é um controlador/extensão e conjunto de ferramentas do Kubernetes que fornece **recursos avançados** de implantação para aplicativos (deployments), como estratégias de **Blue/Green** e **Canary**, além de uma análise e entregra progressiva.

Permite que você faça/execute atualizações de forma controlada e gradativa, minimizando e muito os riscos de Downtime e problemas para os usuários.

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

