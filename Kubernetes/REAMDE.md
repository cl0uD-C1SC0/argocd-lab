# Comandos uteis


## Try POD http get
> 01 - Run & Access nginx pod
```bash
kubectl run --image nginx nginx
kubectl exec -it nginx -- bash
```

> 02 - Exec curl
```bash
# svc-name.namespace.svc.cluster.local:<port-if-exists>
curl flask-app-svc.flask.svc.cluster.local:8080
```

## Expose

## Test Blue Green service:

> 01 - Create a simple nginx pod
```bash
kubectl run nginx --image nginx -n flask-app-hml
```

> 02 - Acess the pod
```bash
kubectl -n flask-app-hml exec -it nginx -- bash
```

> 03 - Active
```bash
curl flask-bluegreen-active-svc.flask-app-hml.svc.cluster.local:80
```

> 04 - Preview
```bash
curl flask-bluegreen-preview-svc.flask-app-hml.svc.cluster.local:80
```

> 05 - Canary:
```bash
curl flask-app-canary-svc.flask-app-hml.svc.cluster.local:8080
```

> 06 - Promote the new version
```bash
kubectl-argo-rollouts promote <-n namespace if exists> <name-of-rollout-deployment>
```

OBS: Após executar o promote, só aguardar.
OBS: NÃO HÁ MANEIRAS AUTOMATIZADA DE EFETUAR ROLLBACK...