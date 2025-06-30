
# ROLLOUTS

01 - Criar projeto chamado flask
02 - Renomear o contexto
```bash
CONTEXT_NAME="argocd-poc-cluster"
$CURRENT_CONTEXT=$(kubectl config get-contexts | tail -n 1 | cut -d" " -f10)
kubectl config rename-context $CURRENT_CONTEXT $CONTEXT_NAME
```

03 - Adicionar no ArgoCD
```bash
ARGOCDURL=$(kubectl get svc argocd-server -n argocd -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
argocd login $ARGOCDURL
argocd cluster add $CONTEXT_NAME --project flask
```

04 - Adicionar 1 repositorio para o rollout (Canary)
```bash
# LINK REPO:
git@github.com:cl0uD-C1SC0/flask-app-hml.git
```

> OBS: Validar se a imagem está apontando para a V1

05 - Nos projetos nas seguintes guias:

- Destionations: Colocar o Cluster recem-adicionado
- Cluster Resource Allow List:
    * Kind: "*"
    * Group: "*"

- Namespace resource allow list:
    * Kind: "*"
    * Group: "*"

06 - Criar projeto:

- Name: flask-app-hml
- Project: flask
- Cluster: Cluster adicionado via CLI
- Repo Url: "repo adicionado anteriormente"
- Target: Head
- Path: (root)
- Sync Options: Create Namespace
- Sync Policy: Automatic & Self heal

07 - Testar Rollback:

- Trocar imagem de v1 para v2 e fazer o Sync/Refresh

08 - Testar Canary deploy

- Trocar imagem de v1 para v3 e fazer o Sync/Refresh
- Acessar a URl várias vezes.

