# SETUP ARGOCD ON AKS CLUSTER

## AWS

> Guide from: https://argo-cd.readthedocs.io/en/stable/getting_started/

- 01 Create a namespace for Argocd:
```bash
kubectl create ns argocd
```

- 02 Apply the raw yamls for Argocd:
```bash
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

- 03 Install ArgoCD CLI (Optional)