#!/usr/bin/env bash

#sudo dockerd
sudo docker-compose -f docker-compose.dev.yml stop
sudo docker-compose -f docker-compose.dev.yml rm --force
sudo docker-compose -f docker-compose.dev.yml up -d --remove-orphans --build

# Below command used by pycharm to create a stable build
#/usr/bin/docker compose -f /home/abhilash/Desktop/SelfProjects/SGB Credit Risk/aaa_codebase_2/docker-compose.dev.yml -p aaa_codebase_2 up -d