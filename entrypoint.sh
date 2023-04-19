#!/bin/bash
python manage.py migrate --check
status=$?
if [[ $status != 0 ]]; then
  python manage.py migrate
fi
exec "$@"

#python manage.py makemigrations && python manage.py migrate && gunicorn todolist.wsgi -w 4 -b 0.0.0.0:8000
