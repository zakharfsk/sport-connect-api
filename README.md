### SportConnect API

This API is built with several technologies including Django, and Django Rest Framework. It also uses several other technologies such as Celery for task management and Redis for caching.

## Running the Project 

To get the SportConnect API running locally, we're using [Docker](https://docker.com). If you're not familiar with Docker, lookout for the useful links below.

Before starting, make sure you have [Docker](https://docker.com) and [Docker Compose](https://docs.docker.com/compose/install/), installed on your machine.

After you have installed Docker and Docker Compose, you can run the project locally with this command from the root of the project:
This command will build your Docker images (if they haven't been built yet) and start the containers defined in `docker-compose.yml`.

If you want to run your containers in the background (detached mode), you can use this command instead:
```bash
docker compose up -d --build
```
If you need to rebuild your Docker images (like after changing your Dockerfile), you can use this command:
```bash
docker compose up --build
```

## What Docker Includes
- API Server (http://localhost:8000)
- API Admin Panel (http://localhost:8000/admin)
- Flower For Celery (http://localhost:5555)
- Redis (http://localhost:6379)
- PostgreSQL (http://localhost:5432)
- Nginx (http://localhost:80)

Admin Panel Credentials:
- Username: root
- Password: root

## Stopping the Project
When you're done working, you can stop your containers with this command:
```bash
docker compose down
```

## Useful Docker Links

- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)