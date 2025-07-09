# 📂 Simple flask APP

O APP utilizado como base neste laboratório ele é bem simples, utilizando a biblioteca Flask, ele vai criar uma rota no **/**, que ao acessar, na porta 8080, mostrará uma mensagem de Hello World.

## Realize o Build

01 - Efetue o Build da primeira versão da imagem:
```bash
docker build -t flask-app .
```

>OBS: Substitua os campos abaixo: "<YOUR_ACCOUNT_ID>" pelo ID da sua conta da AWS que irá utilizar neste laboratório.

02 - Faça login no AWS ECR:
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <YOUR_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
```

03 - Troque a tag de latest para V1 + Apontamento para o AWS ECR
```bash
docker tag flask-app:latest <YOUR_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/flask-app:v1
```

04 - Efetue o Push
```bash
docker push <YOUR_ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/flask-app:latest
```

Realize o Build de três versões:

- v1: Funcionando
- v2: Redirecionamento da porta de 8080 para 8181 (Apenas no Flask)
- v3: Funcionando com o redirecionamento da porta de 8181 para 8080

Essas versões serão utilizadas para você realizar o teste, veja mais detalhes:

| Versão | Objetivo |
---| ---|
flask-app:v1 | Primeira versão da aplicação, será utilizada como base
flask-app:v2 | Versão com algum problema na aplicação, será utilizada para efetuar o Rollback da v2 > v1
flask-app:v3 | Versão nova com alguma mudança, será utilizada para ver na prática o Canary & Blue/Green funcionando.

## Como testar?

Cada versão do APP dita anteriormente tem o seu objetivo, para realizar os testes basta trocar o campo **image** nos manifestos do Canary e Blue/Green, depois disto, visualize em tempo real.

