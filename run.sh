echo ${USER}
docker build -t test_hello:least .
docker run test_hello:least