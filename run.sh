echo ${USER}
sudo usermod -aG docker $USER
sudo reboot
echo 'setup done'
docker build -t test_hello:least .
docker run test_hello:least