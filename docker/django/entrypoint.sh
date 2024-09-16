#!/bin/bash

echo "Running makemigrations ..."
python manage.py makemigrations

echo "Running migrate..."
python manage.py migrate


echo "Creating Superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('app_admin', 'app_admin@email.com', 'app_admin_pass')" | python manage.py shell
echo "Collecting static files into STATIC_ROOT..."
python manage.py collectstatic --noinput

# Run gunicorn server
gunicorn ecommerce.wsgi:application
