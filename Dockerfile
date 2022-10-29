# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster


RUN apt-get update

ENV experiment_id=abc

ENV conn_string=DefaultEndpointsProtocol=https;AccountName=utopstadx;AccountKey=m/0NQLf4Jkfv3TOcQXoBYlKRzLVZF8+I314Fg/C72+jo8Aje9AOmylhJs80rVrVoysWFT5JWkWoq+AStx+lqhQ==;EndpointSuffix=core.windows.net
ENV container_name=kusto
ENV data_storage_info=export_1_ec2832f85bf54e778f6fefeb64e10fe2.csv

ENV seed_storage_info=seed_id_8970087ec6/6057f45b-7308-49af-80a2-241856b7ebf3/seedid.csv


WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "script.py"]