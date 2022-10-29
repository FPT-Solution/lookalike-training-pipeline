import logging
import pandas as pd
from io import BytesIO
from utils.cloud import DataLakeStorage


def mapping_user2score(list_user_id, list_score):
    df = pd.DataFrame({"user_id": list_user_id, "score": list_score})
    return df

def read_data(stream_downloader):
    df = pd.read_csv(BytesIO(stream_downloader.readall()))
    return df

def pick_label(user_id_all ,seed_ids):
    labels = []
    for i in user_id_all:
        if i in seed_ids:
            labels.append(1)
        else:
            labels.append(0)
    return labels

def get_seed_ids(config, col_name_id):
    print('get seed ids.......')
    storage = DataLakeStorage(container_name=config['container_name'], conn_string= config['connection_string'])
    stream_downloader = storage.read_blob(config['blob_name'])
    df_seed_ids = read_data(stream_downloader = stream_downloader)
    print('df seed id: {}'.format(df_seed_ids))
    seed_ids = df_seed_ids[col_name_id].to_list()
    return seed_ids