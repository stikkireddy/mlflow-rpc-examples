# basic-fastapi-app


## Instructions

```bash
pip install -U 'mlrpc[cli]'
```

1. `mlrpc deploy -p <profile>`: This will deploy the artifacts to databricks
2. `mlrpc local -p <profile>`: This will verify the artifacts in a local server
3. `mlrpc serve -p <profile>`: This will serve the artifacts in a serverless model serving infra
4. `mlrpc swagger -p <profile>`: This will generate a swagger UI for the remote endpoint