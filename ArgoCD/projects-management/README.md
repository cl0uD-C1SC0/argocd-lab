## ARGOCD PROJECTS

Os projetos no ArgoCD são uma forma de organização para facilitar o gerenciamento das aplicações em diversos clusters Kubernetes.

Cada projeto tem seus próprios repositórios, clusters de Kubernetes, permissões, janelas de sicronização e eventos, veja abaixo em detalhes

⚠️ DOCUMENTAÇÃO AINDA EM CONSTRUÇÃO ⚠️

### Como criar

- 01 - Acesse o ArgoCD
- 02 - Na lateral esquerda vá para Settings
- 03 - Clique no botão de **New project**

> Padrão de nome pode ser definido pela política da empresa, mas para exemplo, poderíamos colocar o nome do time ou produto que compõe diversos microsserviços dentro, exemplo: cartoes

> Sempre que possível coloque uma Descrição a respeito do projeto, contendo o nome dos responsáveis, desenvolvedores e Tech Lead responsável.

### Source repositories vs Scoped repositories

**Source repositories:** 