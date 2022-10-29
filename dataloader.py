import pandas as pd
from io import BytesIO
from utils.common import pick_label
from utils.cloud import DataLakeStorage
import logging

# TODO load data from Kusto
# require: 
# 1. setup function: có connection để kết nối tới adx
# 2. load function: có bảng feature để thực hiện query
# 3. loget_data_train: đảm bảo có index, feature và lable column

class KustoDataloader:
    pass

class DefaultDataLoader:

    def __init__(self, config):
        self.config = config
        self.data = None
        self.storage = DataLakeStorage(config['container_name'], config['connection_string'])
        
    def load(self, fill_nan = True):
        try:
            stream_downloader = self.storage.read_blob(blob_name=self.config['blob_name'])
            data = pd.read_csv(BytesIO(stream_downloader.readall()))
            #TODO Fill Nan function
            if fill_nan == True:
                data = data.fillna(0)
            return data
        
        except Exception as e:
            self.status = 500
            raise Exception("Exception when load data. Reason: {}".format(e))

    def get_data_train(self, seed_ids):
        self.data = self.load()
        logging.info('test: {}'.format(self.data))
        logging.info('type: {}'.format(type(self.data)))
        # default index is first columns
        data_index = self.data.iloc[:, 0].to_list()
        # default features are columns from 2 -> tail
        data_feature = self.data.iloc[:, 1:]
        data_label = pick_label(data_index, seed_ids)
        return data_index, data_feature, data_label