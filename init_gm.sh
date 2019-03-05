#!/bin/bash

USERNAME="root"
PASSWORD="123456"
DBNAME="managemen"

#创建数据库
create_db_sql="CREATE DATABASE ${DBNAME} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;"
mysql -u${USERNAME} -p${PASSWORD} -e "${create_db_sql}"

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

