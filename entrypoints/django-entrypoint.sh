#!/bin/sh

set -o errexit
set -o nounset

echo "Migrate collect static..."
python manage.py collectstatic --noinput &&

echo "Migrate..."
python manage.py migrate --noinput &&

echo "Create superuser..."
python manage.py createsuperuser --noinput &&

echo "Load fixtures..."
python -Xutf8 manage.py loaddata ./fixtures/core.json &&

echo "Starting server..."
gunicorn 'sport_connect_api.wsgi' --reload --bind=0.0.0.0:8000
