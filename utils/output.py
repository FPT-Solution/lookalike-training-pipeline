from utils.cloud import DataLakeStorage

# TODO module upload output
def make_output_score_path(experiment_id, run_id):
    return '{}/{}/output_score.csv'.format(experiment_id, run_id)


def store_output(conn_string, container_name, experiment_id, run_id, df):
    url_path = make_output_score_path(experiment_id, run_id)
    print(url_path)
    storage = DataLakeStorage(container_name=container_name, conn_string=conn_string)
    storage.upload_blob(blob_name = url_path, data=df.to_csv(index = False))
    return url_path