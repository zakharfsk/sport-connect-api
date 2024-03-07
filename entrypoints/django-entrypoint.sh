#!/bin/sh

set -o errexit
set -o nounset

echo "Migrate collect static..."
python /app/manage.py collectstatic --noinput &&

echo "Migrate..."
python /app/manage.py migrate --noinput &&

echo "Create superuser..."
python /app/manage.py createsuperuser --noinput &&

echo "Load fixtures..."
python -Xutf8 /app/manage.py loaddata ./fixtures/core.json &&

echo "Starting server..."
gunicorn 'app.sport_connect_api.wsgi' --reload --bind=0.0.0.0:8000
