sudo systemctl enable docker
sudo service docker stop
sudo rm -rf /var/run/docker.pid
sudo rm -rf /var/lib/docker/volumes/metadata.db
sudo dockerd
