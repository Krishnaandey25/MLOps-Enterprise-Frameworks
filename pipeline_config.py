import mlflow

def train_and_log():
    with mlflow.start_run():
        mlflow.log_param('learning_rate', 0.01)
        mlflow.log_metric('accuracy', 0.95)
        print('Training logged to MLflow')

if __name__ == '__main__':
    train_and_log()