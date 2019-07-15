##Run mySQL docker
```
docker-compose up -d
docker ps
```




##Create DB and tables
```
mysql -u root -pexample -e "CREATE DATABASE GEOLOCATION"
mysql -u root -pexample -D geolocation < /usr/sql/tables.sql
```
or open UI: http://localhost8080
and create database and table using the web interfaces