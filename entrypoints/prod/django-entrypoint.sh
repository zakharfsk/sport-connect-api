#!/bin/sh

set -o errexit
set -o nounset

echo "Migrate collect static..."
python /sport-connect-api/manage.py collectstatic --noinput &&

echo "Migrate..."
python /sport-connect-api/manage.py migrate --noinput &&

echo "Create superuser..."
python /sport-connect-api/manage.py createsuperuser --noinput &&

echo "Load fixtures..."
python -Xutf8 /sport-connect-api/manage.py loaddata ./fixtures/core.json &&

echo "Starting server..."
gunicorn 'sport-connect-api.sport_connect_api.wsgi' --reload --bind=0.0.0.0:8000
