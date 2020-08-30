So when trying to setup vscode with docker compose what you do first is have a docker-compose file. For example my
setup is:

docker-compose which holds services
in this case I've got backend service with fast api that has got notes crud

and another postgresql service
The file is:

```
version: "3.7"

services:
  web:
    build: ./services/backend
    command: uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
    volumes:
      - ./services/backend:/usr/src/app
    ports:
      - 8002:8000
    environment:
      - DATABASE_URL=postgresql://hello_fastapi:hello_fastapi@db/hello_fastapi_dev
  db:
    image: postgres:12.1-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER=hello_fastapi
      - POSTGRES_PASSWORD=hello_fastapi
      - POSTGRES_DB=hello_fastapi_dev

volumes:
  postgres_data:

```


In order to run this docker compose I need the Remote extension for vscode, then open the folder where this docker
compose is and extend it running the web service.

This will create devcontainer folder with couple of files, docker-compose extension and devcontainer. There's no need to
change any of these files for now.

Next we need vscode setup in order to run debug and pytest for example.
To use the debug we need launch config file:

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Fast API",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "cwd": "${workspaceFolder}/services/backend/",
            "args": [
                "app.main:app",
                "--reload",
            ],
        }
    ]
}
```

For fast api we need uvicorn as the module, the correct directory where the executable file is located (cwd) and 
args.

uvicorn app.main:app --reload  (To start Fast API app with uvicorn server)

And settings.json file which gets created when choosing black as autoformatter and choosing python interpreter. Here I 
am adding pytest config to be able to find the tests with the vscode test extension.

```
{
    "python.pythonPath": "/usr/local/bin/python",
    "python.formatting.provider": "black",
    "python.testing.unittestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.pytestEnabled": true
}
```

And that's about it for now. Next is to add react app and maybe some other microservices like auth etc.
