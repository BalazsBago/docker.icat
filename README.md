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

# Access
### Web admin
Payara admin access is available on: https://localhost:4848   
The user is admin.   
Script to obtain the password:   
```shell
echo $(docker-compose -f docker-compose.yaml exec webserver cat .gfclient/pass | grep asadmin | awk '{print $2}' | base64 -d -i)
```
### Topcat 
Topcat server is available on: http://localhost:8080    
Anonymous and simple authentication methods are enabled with the provided configurations.
Simple user is 'usera' and the password is 'passworda'.

# Ingestion 
### Fill up with dummy data
Run the following script in the directory of the script with using pipenv. The Pipfile and
the lock files are provided as well.  
This script will fill up your database with some dummy data.   
(1 facility, 3 investigations and 1 dataset per investigation)

# TODO:

- add more dummy data
- use large data files (> 10GB) 
- add parameters
- add users and permissions
- persistent volume option for the compose file

