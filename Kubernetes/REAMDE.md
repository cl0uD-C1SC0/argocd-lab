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
