# basic-fastapi-app


## Instructions

```bash
pip install -U 'mlrpc[cli]'
```

1. Run the setup_db.py to populate data in data/chroma folder with data for chroma db
2. `mlrpc deploy -p <profile>`: This will deploy the artifacts to databricks
3. `mlrpc local -p <profile>`: This will verify the artifacts in a local server
4. `mlrpc serve -p <profile>`: This will serve the artifacts in a serverless model serving infra
5. `mlrpc swagger -p <profile>`: This will generate a swagger UI for the remote endpoint