from azure.storage.blob import BlobServiceClient
from typing import Iterable

class DataLakeStorage:

    def __init__(self, container_name, conn_string):
        self.blob_service_client = None
        self.container_client = None
        self.setup(container_name, conn_string)

    def setup(self, container_name, conn_string):
        print(conn_string)
        self.blob_service_client = BlobServiceClient.from_connection_string(conn_string)
        self.container_client = self.blob_service_client.get_container_client(container_name)

    def read_blob(self, blob_name: str):
        blob_client = self.container_client.get_blob_client(blob_name)
        stream_downloader = blob_client.download_blob()
        return stream_downloader

    def upload_blob(self, blob_name: str, data: Iterable, overwrite=True):
        blob_client = self.container_client.get_blob_client(blob=blob_name)
        blob_client.upload_blob(data=data, overwrite=overwrite)

    def delete_blob(self, blob_name: str):
        blob_client = self.container_client.get_blob_client(blob=blob_name)
        blob_client.delete_blob()