#!/bin/sh

set -o errexit
set -o nounset

echo "Starting celery worker..."
(cd ./sport_connect_api && celery \
  -A sport_connect_api.celery \
  worker \
  --loglevel=DEBUG \
  -P gevent -E -c 1000
  )