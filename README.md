Development
    docker build . -f Dockerfile.dev --tag sre-mehran:dev
    docker run -p 8081:8000 --name sm-dev -v "$(PWD)"/src:/usr/src/code sre-mehran:dev 

Production
    docker build . -f Dockerfile.live --tag sre-mehran:live
    docker run -p 8000:8000 --name sm-live sre-mehran:live 
