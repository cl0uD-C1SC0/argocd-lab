# ArgoCD

Index:
* [ArgoCD Roles and Accounts Info](#argocd-roles-and-accounts-management)
* [Criando um usuário](#criando-um-usuário)
* [Desativando um usuário](#desativando-um-usuário)
* [Boas práticas de Usuarios](#boas-práticas-de-usuário)
* [Permissões no ArgoCD](#permissões-no-argocd)
* [Roles](#roles)
* [Resources](#resources-recursos)
* [Action](#action-ações)
* [Object](#object-objeto)
* [Effect](#effect-efeito)
* [Exemplos práticos](#exemplos-práticos)
* [Boas práticas de Roles](#boas-práticas-de-roles)

## ARGOCD ROLES AND ACCOUNTS MANAGEMENT

Neste guia você verá como criar usuário, gerenciar o usuário, colocar permissões, criar permissões e outros pontos importantes sobre o gerenciamento de permissões e usuários no ArgoCD

### CRIANDO UM USUÁRIO

O ArgoCD suporta dois tipos de autenticação: **Local = argocd-cm (ConfigMap)** ou **SSO/OIDC = argocd-rbac-cm (ConfigMap)**

Neste Laboratório vamos estar utilizando o Local, por ser mais simples. Siga o passo-a-passo abaixo para criar um usuário simples

> OBS: Arquivo de exemplo: [argocd-cm.yaml](./argocd-cm.yaml)

- 01: Edite o configMap (argocd-cm)
```bash
kubectl edit -n argocd configmap argocd-cm
```

- 02: após o *data*, adicione: accounts.devuser: apiKey, login
```bash
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-cm
  namespace: argocd
  labels:
    app.kubernetes.io/name: argocd-cm
    app.kubernetes.io/part-of: argocd
data:
  accounts.devuser: apiKey, login
  ...
  ...
```

OBS:
> **accounts.<nome_do_usuario>** = Define o nome do usuário
> **apiKey** = Permite a criação de um Token, utilizado mais a frente em repositorios/projetos
> **login** = Permite o usuário faça Login na UI (Interface Gráfica do ArgoCD)

<br>

- 03: Salve e feche o arquivo

<br>
<br>

Para definir a senha do usuário, será necessário instalar a linha de comando do ArgoCD, execute:
```bash
curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
rm argocd-linux-amd64
```

<br>

- 04: Faça Login no ArgoCD
```bash
ARGOCDURL=$(kubectl get svc argocd-server -n argocd -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
argocd login $ARGOCDURL
```

- 04: Defina senha do usuário:
```bash
argocd account update-password --account devuser --new-password novaSenha
```

- (Opcional): Você também pode forçar uma nova senha:
```bash
argocd account update-password --account devuser
```

- 05: Teste o Login com o usuário devuser no ArgoCD

### Desativando um usuário

- 01: Para remover/desativar um usuário, basta remover a linha do accounts.<user_name>
```bash
# ANTES
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-cm
  namespace: argocd
  labels:
    app.kubernetes.io/name: argocd-cm
    app.kubernetes.io/part-of: argocd
data:
  accounts.devuser: apiKey, login

# DEPOIS
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-cm
  namespace: argocd
  labels:
    app.kubernetes.io/name: argocd-cm
    app.kubernetes.io/part-of: argocd
data:
  # LINHA REMOVIDA
```

- 02: Execute um rollout restart no ArgoCD agora:
```bash
kubectl rollout restart deployment argocd-server -n argocd
```

### BOAS PRÁTICAS DE USUÁRIO

✅ 01 - Permissões no argocd-cm
* login: Permite Login via UI ou CLI
* apiKey: Permite gerar Tokens para API ou CI/CD.
* updatePassword: Permite que o usuário troque sua senha (recomendado)
* logout: Permite logout remoto do usuário

✅ 02 - Nomes:
* Utilizar nomes padronizados
* Não utilizar uma conta para mais de um usuário

✅ 03 - Senhas:
* Crie senhas fortes misturando letras maiúsculas, minúsculas, números e letras especiais.
* Jamais salve em repositório

✅ 04 - API Keys:
* Utilize os Tokens para automatizações, nunca utilize uma conta de um usuário.

✅ 05 - Revisão:
* Delete usuários não utilizados
* Revise os usuários locais
* Se possível utilizar OIDC/SSO

## PERMISSÕES NO ARGOCD

Todas as permissões no ArgoCD seguem um padrão e devem ser aplicadas ao arquivo **argocd-rbac-cm***.

Sintaxe:
> p, <role>, <resource>, <action>, <object>, <effect>

| Campo        | O que significa                                                          |
| ------------ | ------------------------------------------------------------------------ |
| `p`          | Define que é uma permissão (policy)                                      |
| `<role>`     | Nome do role (pode ser global ou scoped por projeto)                     |
| `<resource>` | Tipo de recurso no ArgoCD (applications, clusters, etc)                  |
| `<action>`   | Ação permitida (get, create, update, delete, sync, override, etc)        |
| `<object>`   | Escopo do objeto, ex: `*` para todos ou `dev/*` para apps do projeto dev |
| `<effect>`   | allow ou deny                                                            |

### Roles

Elas podem ser nível global:
```bash
role:readonly
```

Ou a nível de projeto:
```bash
proj:dev:readonly
```

### Resources (Recursos)

| Resource     | O que controla                                  |
| ------------ | ----------------------------------------------- |
| applications | Aplicações do ArgoCD                            |
| clusters     | Clusters cadastrados no ArgoCD                  |
| repositories | Repositórios cadastrados                        |
| projects     | Projetos (AppProject CRDs)                      |
| certificates | Certificados TLS cadastrados                    |
| accounts     | Contas de usuários                              |
| gpgkeys      | GPG keys no ArgoCD                              |
| exec         | Execução de comandos remotos via ArgoCD (risky) |

### Action (ações)

| Action     | O que permite fazer           |
| ---------- | ----------------------------- |
| get        | Ver a aplicação               |
| create     | Criar nova aplicação          |
| update     | Alterar aplicação existente   |
| delete     | Deletar aplicação             |
| sync       | Sincronizar (deploy)          |
| override   | Sobrescrever settings no sync |
| rollback   | Reverter release              |
| refresh    | Atualizar status da aplicação |
| action/run | Executar ações customizadas   |

### Object (objeto)

- **`*`** = Todos
- **dev/`*`** = Tudo dentro do projeto dev
- **myapp** = Aplicação específica

### Effect (efeito)

Os efeitos podem ser
> allow (Permitir)
> deny (Negar)

Por padrão, sempre será **deny**

### EXEMPLOS PRÁTICOS

01 - **Visualização** somente no projeto dev:
```bash
p, proj:dev:readonly, applications, get, dev/*, allow
g, devuser, proj:dev:readonly
```
| Campo               | Significado                       |
| ------------------- | --------------------------------- |
| p                   | policy line                       |
| proj\:dev\:readonly | role readonly no projeto dev      |
| applications        | recurso de aplicações             |
| get                 | ação: leitura                     |
| dev/\*              | escopo: todas apps do projeto dev |
| allow               | efeito: permite                   |

> Efeito: Essa permissão só permite que o usuário devuser, visualize o projeto dev

02 - **Permitir** acesso ao botão **sync** e **create app** no projeto frontend:
```bash
p, proj:frontend:deploy, applications, create, frontend/*, allow
p, proj:frontend:deploy, applications, sync, frontend/*, allow
g, devuser, proj:frontend:deploy
```

03 - Acesso **admin** completo no projeto backend:
```bash
p, proj:backend:admin, applications, *, backend/*, allow
g, devuser, proj:backend:admin
```

04 - Acesso **admin** no ArgoCD inteiro:
```bash
p, role:admin, *, *, *, allow
g, devuser, role:admin
```

05 - Permissão apenas para gerenciar os clusters:
```bash
p, role:cluster-admin, clusters, *, *, allow
g, devuser, role:cluster-admin
```

Quando quisermos aplicar essas permissões em algum usuário, utilizaremos a seguinte sintaxe:
```bash
g, <usuario>, <role>
# Exemplo:
g, devuser, role:cluster-admin
g, devuser, proj:frontend:deploy
```

Se quisermos adicionar mais de um usuário em uma role, faremos assim:
```bash
g, usuario1, role
g, usuario2, role
g, usuario3, role
```
### BOAS PRÁTICAS DE ROLES

✅ 01 - Utilize o principio de Least Privilege
* - Conceda apenas o necessário para o usuário realizar suas funções.

✅ 02 - Roles por função, não por usuário
* - Crie roles genéricas como: developer, admin, release-manager
* - Atribua essa roles aos usuários corretos.

✅ 03 - Evite utilizar admin global
* - Dê admin por projeto
* - Admin global ficará responsável pelo time de SRE/DevOps

✅ 04 - Gerencie usuários e RBAC via GitOps
* - Configure o os arquivos: argocd-cm.yaml & argocd-rbac-cm.yaml versionados em GIT
* - Motivo: Facilita rastreabilidade, backup e REVIEW sempre que um usuário ou permissão for alterado.

✅ 05 - Revise semanalmente, mensalmente
* - Sempre revise os usuários que tem acesso e suas permissões
* - Usuário que entrou de férias deve ser desabilitado.
* - Usuário que foi desligado, também deve ser desabilitado

✅ 06 - Utilizar SSO/OIDC para autenticação.

