echo ${USER}

echo 'setup environment by docker image'
echo 'starting......'
docker build  -t ahihi:123  --no-cache .
echo 'Setup successfuly!!!'
echo 'executing container......'
docker run -e experiment_id=test_manhdhd  -e connect_string="DefaultEndpointsProtocol=https;AccountName=utopstadx;AccountKey=m/0NQLf4Jkfv3TOcQXoBYlKRzLVZF8+I314Fg/C72+jo8Aje9AOmylhJs80rVrVoysWFT5JWkWoq+AStx+lqhQ==;EndpointSuffix=core.windows.net" -e container_name="kusto" -e seed_storage_info="seed_id_8970087ec6/6057f45b-7308-49af-80a2-241856b7ebf3/seedid.csv" -e data_storage_info="export_1_ec2832f85bf54e778f6fefeb64e10fe2.csv" ahihi:123