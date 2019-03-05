#!/bin/sh

# python manage.py makemigrations

# python manage.py migrate

# python manage.py init_admin

# python manage.py import_data

# python manage.py runserver 0.0.0.0:3032 --settings=waxiao.settings_dev

gunicorn -b :8080 management.wsgi:application

