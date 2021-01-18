import click

from ml.utils import train_application_classification_cnn_model, train_traffic_classification_cnn_model
from config import *

@click.command()
@click.option('-d', '--data_path', default=train_test_data, help='training data dir path containing parquet files', required=False)
@click.option('-m', '--model_path', default=model_path, help='output model path', required=False)
@click.option('-t', '--task', default="traffic", help='classification task. Option: "app" or "traffic"', required=False)
@click.option('--gpu', help='whether to use gpu', default=True, type=bool)
def main(data_path, model_path, task, gpu):
    if gpu:
        gpu = -1
    else:
        gpu = None
    if task == 'app':
        train_application_classification_cnn_model(
            data_path + "application_classification/train.parquet",
            model_path + "application_classification.cnn.model", gpu)
    elif task == 'traffic':
        train_traffic_classification_cnn_model(
            data_path + "traffic_classification/train.parquet",
            model_path + "traffic_classification.cnn.model", gpu)
    elif task == 'both':
        train_application_classification_cnn_model(
            data_path + "application_classification/train.parquet",
            model_path + "application_classification.cnn.model", gpu)
        train_traffic_classification_cnn_model(
            data_path + "traffic_classification/train.parquet",
            model_path + "traffic_classification.cnn.model", gpu)
    else:
        exit('Not Support')


if __name__ == '__main__':
    main()
