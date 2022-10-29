echo ${USER}
sudo chown root:docker /var/run/docker.sock
echo 'setup done'
docker build -t test_hello:least .
docker run test_hello:least