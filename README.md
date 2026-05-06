# Request Systems API

  

## Como executar a aplicação

  

1. Certifique-se de ter o `uv` instalado. Caso não tenha, instale-o com:

```bash

pip  install  uv

```

  

2. Na raiz do projeto, sincronize o ambiente e instale as dependências executando:

  

```bash

uv  sync

```

  

3. Inicie o servidor através do script de entrada:

  

```bash

uv  run  entrypoint.py

```

  

## Configuração das Variáveis de Ambiente

  

Para a conexão com o Databricks, é necessário configurar as variáveis de ambiente. Você pode fazer isso criando um arquivo `.env` na raiz do projeto, usando o `.env.example` como modelo:

  

```bash

cp  .env.example  .env

```

  

Preencha o arquivo `.env` com suas credenciais e configurações do Databricks. As variáveis esperadas são:

  

-  `DATABRICKS_TOKEN`

-  `DATABRICKS_HOST`

-  `DATABRICKS_HTTP_PATH`

-  `DATABRICKS_CATALOG`

-  `DATABRICKS_SCHEMA`

  
  

## Acesso à documentação (Swagger / ReDoc)

  

Com a aplicação em execução, você pode acessar a documentação interativa da API pelo navegador nos seguintes links:

  

- Swagger UI: http://0.0.0.0:8000/docs

- ReDoc: http://0.0.0.0:8000/redoc
