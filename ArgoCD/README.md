# ArgoCD

## MENU:


## Add context/cluster no ArgoCD

> 01 - Renomeie o contexto existe
```bash
kubectl config get-contexts
kubectl config rename-context <contexto_atual> <nome_novo>
```

> 02 - Faça login no ArgoCD
```bash
ARGOCDURL=$(kubectl get svc argocd-server -n argocd -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
argocd login $ARGOCDURL
```

> 03 - Adicione um novo contexto/cluster no ArgoCD em um projeto especifico
```bash
argocd cluster add <CONTEXT_NAME> --project <PROJECT_NAME>
```