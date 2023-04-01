#!/usr/bin/env bash


IAM_PORT=8000
SOUTH_GERMAN_BANK_PORT=8001
NOTIFICATIONS_PORT=8002
MESSAGES_PORT=8003
TRANSACTIONS_PORT=8004

IAM_SERVICE="IAM"
SOUTH_GERMAN_BANK_SERVICE="SOUTH_GERMAN_BANK"
NOTIFICATIONS_SERVICE="NOTIFICATIONS"
MESSAGES_SERVICE="MESSAGES"
TRANSACTIONS_SERVICE="TRANSACTIONS"

#../iam/manage.py runserver ${IAM_PORT}

docker rm my_container
docker rmi my_image
gnome-terminal --tab --title=${DockerD} -e "bash -c 'sudo dockerd' <&-& ' sudo docker-compose -f docker-compose.dev.yml down' <&-&-& ' sudo docker build -t akatsuki ../'"

gnome-terminal --tab --title=${IAM_SERVICE} -e "bash -c 'iam/manage.py runserver ${IAM_PORT}'"
#gnome-terminal --tab --title=${SOUTH_GERMAN_BANK_SERVICE} -- "bash -c './SouthGermanBank/manage.py runserver ${SOUTH_GERMAN_BANK_PORT}'"

#gnome-terminal --tab --title="Terminal 1" -e "bash -c 'command1'"
#gnome-terminal --tab --title="Terminal 2" -e "bash -c 'command2'"