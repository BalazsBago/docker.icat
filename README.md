# A docker-compose setup to start a demo iCat system

The compose file describes three services:
- **database_icat**: This is a MySQL database for the **icat server** based on mysql:5.7 image on docker hub.
- **database_topcat**: This is a MySQL database for the **topcat** based on mysql:5.7 image on docker hub.
- **webserver**: This is a Payara application server based on a local build of the provided Dockerfile.

## Services
### Start services
Use the following script in the directory of the project.
```shell
docker-compose -f docker-compose.yaml up -d
```
### Access logs
Use the following script in the directory of the project.
```shell
docker-compose -f docker-compose.yaml logs -f
```
However, this is not so useful, because application logs are not visible via docker logs.
### Build the webserver
Use the following script in the directory of the project.
```shell
docker-compose -f docker-compose.yaml build webserver
```
### Restart after only configuration change
Use the following script in the directory of the project.
```shell
docker-compose -f docker-compose.yaml restart webserver
```
### Stop services
Use the following script in the directory of the project.
```shell
docker-compose -f docker-compose.yaml down
```
## Admin access
Payara admin access is available on: https://localhost:4848   
The user is admin.   
Script to obtain the password:   
```
echo $(docker-compose -f docker-compose.yaml exec webserver cat .gfclient/pass | grep asadmin | awk '{print $2}' | base64 -d -i)
```
## Topcat access
Topcat server is available on: http://localhost:8080    
Anonymous and simple authentication methods are enabled with the provided configurations.
Simple user is 'usera' and the password is 'passworda'.

## Ingest some dummy data
...