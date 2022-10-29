echo ${USER}
sudo chown root:docker /var/run/docker.sock
docker build -t test_hello:least .
docker run test_hello:least