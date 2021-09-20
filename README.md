**Development**
* docker build . -f Dockerfile.dev --tag sre-mehran:dev
* docker run -p 8081:8000 --name sm-dev -v "${PWD}/src":"/usr/src/code" -it sre-mehran:dev 
* docker run -p 8081:8000 --name sm-dev -v "${PWD}/src":"/usr/src/code" -d sre-mehran:dev 

**Production**
* docker build . -f Dockerfile.live --tag sre-mehran:live
* docker run -p 8000:8000 --name sm-live -d sre-mehran:live 

**Database** \
docker run --name db -e POSTGRES_PASSWORD=3210 -e POSTGRES_USER=mehran -e POSTGRES_DB=db -v db:"/var/lib/postgresql/data" -p 8082:5432 -d postgres:13.4-alpine