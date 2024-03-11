#!/bin/sh

set -o errexit
set -o nounset

echo "Migrate collect static..."
python ./sport_connect_api/manage.py collectstatic --noinput &&

echo "Migrate..."
python ./sport_connect_api/manage.py migrate --noinput &&

echo "Load fixtures..."
python -Xutf8 ./sport_connect_api/manage.py loaddata ./sport_connect_api/fixtures/core.json &&

echo "Starting server..."
(cd ./sport_connect_api && gunicorn 'sport_connect_api.wsgi' --reload --bind=0.0.0.0:8000)