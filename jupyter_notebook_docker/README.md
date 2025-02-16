# Jupyternotebook in Docker
## Spinup standalone jupyter notebook in docker
```
docker run --rm -p 8889:8888 -v $(pwd)/jupyter-data:/home/jovyan/work quay.io/jupyter/base-notebook start-notebook.py --NotebookApp.token='my-token'
```

## Including python library in notebook
Install libraries from `requirements.txt` along with volume mapping via docker compose:
```
docker-compose up -d
```
Access notebook and enter token as mentioned on compose file: http://0.0.0.0:8889/
