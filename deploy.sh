#!/bin/bash
set -e

cd /home/ubuntu/flask-docker-app

git pull origin main

docker stop flask-app || true
docker rm flask-app || true

docker build -t flask-app .
docker run -d --name flask-app -p 5000:5000 flask-app
