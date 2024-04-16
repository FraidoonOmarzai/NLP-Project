from datetime import datetime
import os


# Common Constants
TIMESTAMP: datetime = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
ARTIFACTS_DIR = os.path.join('artifacts', TIMESTAMP)
BUCKET_NAME = 'hatedataset'
S3_DATA_FOLDER = 'data'
S3_FILE = 'dataset.zip'


# Data Ingestion Constants
DATA_INGESTION_DIR = os.path.join(ARTIFACTS_DIR, 'DataIngestion')
IMBALANCE_DATA = 'imbalanced_data.csv'
RAW_DATA = 'raw_data.csv'
