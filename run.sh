echo ${USER}
sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
docker build -t test_hello:least .
docker run test_hello:least