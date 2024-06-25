#!/bin/bash

compose_file="docker-compose.yml"
docker stop sleepyBot
docker rm sleepyBot

if [[ $* == *--prune* ]]; then
    docker system prune -a
fi

# Check if --D flag is provided
if [[ $* == *--D* ]]; then
    compose_file="docker-compose-dev.yml"
fi
if [[ $* == *--L* ]]; then
    compose_file="docker-compose-local.yml"
fi


# Start Docker container
docker-compose -f "$compose_file" up -d --build
docker ps -a
