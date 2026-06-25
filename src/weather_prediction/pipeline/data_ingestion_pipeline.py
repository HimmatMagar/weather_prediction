from weather_prediction import logger
from weather_prediction.components.data_ingestion import DataIngestion
from weather_prediction.config import ConfigurationManager


STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline():
      def __init__(self):
            pass

      def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.getDataIngestionConfig()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.unzip_file()
            
if __name__ == "__main__":
      try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            obj = DataIngestionPipeline()
            obj.main()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<")
      except Exception as e:
            logger.exception(e)
            raise e