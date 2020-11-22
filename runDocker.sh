#!/bin/bash

# Evaluates 
if [ ! -f "./docker-compose.yml" ] 
then
    echo "[ERROR] - File ./docker-compose.yml not found"
    echo "[INFO] - Execute script at same level folder where it belongs"
    exit 1
fi

# Build and instance containers with docker-compose info
docker-compose up -d --build

# Create database entities
docker-compose exec web python manage.py migrate