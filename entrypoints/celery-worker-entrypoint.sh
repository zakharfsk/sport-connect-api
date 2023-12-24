#!/bin/sh

echo "Starting celery worker..."

celery -A sport_connect_api.celery worker --loglevel=DEBUG -P gevent -E -c 1000