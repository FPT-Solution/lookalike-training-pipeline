from dataloader import DefaultDataLoader
from experiment import Experiment
from utils.output import store_output
from utils.common import mapping_user2score, get_seed_ids
import os

def run():
    experiment_id = os.environ.get('experiment_id')
    conn_string = os.environ.get('conn_string')
    container_name = os.environ.get('container_name')
    data_storage_info = os.environ.get('data_storage_info')
    seed_storage_info =  os.environ.get('seed_storage_info')

    seed_config = {
        "container_name": container_name,
        "connection_string": conn_string,
        'blob_name': seed_storage_info
    }

    seed_ids = get_seed_ids(config = seed_config, col_name_id='seed_id')

    data_config = {
        "container_name": container_name,
        "connection_string": conn_string,
        'blob_name': data_storage_info
    }

    dataloader = DefaultDataLoader(data_config)
    user_ids, X, y = dataloader.get_data_train(seed_ids = seed_ids)
    
    experiment = Experiment(run)
    similarity_score = experiment.execute(X, y)
    df_score = mapping_user2score(user_ids, similarity_score)
    # store output
    store_output(conn_string = conn_string, container_name = container_name, experiment_id = experiment_id, run_id = "test", df = df_score)
if __name__ == '__main__':
    run()