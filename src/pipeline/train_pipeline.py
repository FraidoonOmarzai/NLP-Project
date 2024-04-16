from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import (DataIngestionConfig,)
from src.entity.artifact_entity import (DataIngestionArtifact,)

import sys


class TrainingPipeline:
    """Class representing a training pipeline.

    This class orchestrates the various steps involved in the training pipeline,
    including data ingestion, data transformation and further processing.

    Methods:
        start_data_ingestion: Starts the data ingestion process.
    """

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info("starting data ingestion")
            data_ingestion = DataIngestion(
                self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.init_data_ingestion()

            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys)

    def run_pipeline(self):
        logging.info("running training pipeline")
        try:
            # data ingestion Sections
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise CustomException(e, sys)
