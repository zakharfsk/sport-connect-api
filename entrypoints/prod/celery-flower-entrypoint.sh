#!/bin/bash

set -o errexit
set -o nounset

worker_ready() {
    celery -A sport_connect_api.celery inspect ping
}

until worker_ready; do
  >&2 echo 'Celery workers not available'
  sleep 1
done
>&2 echo 'Celery workers is available'

celery \
  --broker=amqp://guest:guest@rabbitmq:5672/ \
  flower \
  --broker_api=http://guest:guest@rabbitmq:15672/api/ \
  --debug \
  --persistent=True \
  --db=./flower.db \
  --state_save_interval=10000 \
  purge_offline_workers=10s
