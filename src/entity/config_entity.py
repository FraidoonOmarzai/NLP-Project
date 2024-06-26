from src.constants import *
import os


class DataIngestionConfig:
    """Data class for configuring data ingestion parameters.

    This class provides a convenient way to configure parameters related to data ingestion,
    such as directory paths and S3 bucket names.

    args:
        s3_data_folder (str): The folder path within the S3 bucket containing the data.
        bucket_name (str): The name of the S3 bucket.
        data_ingestion_path (str): The full path to the data within the artifacts directory.
        zip_path (str): The path to the zip file containing the data.
        unzip_path (str): The path to store the unzip files.
        imbalanced_data (str): The path to imbalance_data.cvs file.
        raw_data (str): The path to the raw_data.csv file.
    """

    def __init__(self) -> None:
        self.s3_data_folder = S3_DATA_FOLDER
        self.bucket_name = BUCKET_NAME
        self.s3_file = S3_FILE

        self.data_ingestion_path = os.path.join(
            DATA_INGESTION_DIR, self.s3_data_folder)

        self.zip_path = os.path.join(
            DATA_INGESTION_DIR, self.s3_data_folder, self.s3_file)
        self.unzip_path = os.path.join(DATA_INGESTION_DIR)
        self.imbalanced_data: str = os.path.join(DATA_INGESTION_DIR, IMBALANCE_DATA)
        self.raw_data: str = os.path.join(DATA_INGESTION_DIR, RAW_DATA)
