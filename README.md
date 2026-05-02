# Request Systems API

## Como executar a aplicação

1. Certifique-se de ter o `uv` instalado. Caso não tenha, instale-o com: 
```bash
pip install uv
```

2. Na raiz do projeto, sincronize o ambiente e instale as dependências executando:

```bash
uv sync
```

3. Inicie o servidor através do script de entrada:

```bash
uv run entrypoint.py
```

## Acesso à documentação (Swagger / ReDoc)

Com a aplicação em execução, você pode acessar a documentação interativa da API pelo navegador nos seguintes links:

- Swagger UI: http://0.0.0.0:8000/docs
- ReDoc: http://0.0.0.0:8000/redoc
