from weather_prediction.entity import *
from weather_prediction.constants import *
from weather_prediction.utils import *


class ConfigurationManager:

    def __init__(self, config = config, params = params, schema = schema):
        self.config = read_yaml(config)
        self.params = read_yaml(params)
        self.schema = read_yaml(schema)

        create_dir([self.config.root])

    def getDataIngestionConfig(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_dir([config.root_dir])

        data_ingestion = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            zip_file = config.zip_file,
            unzip_file = config.unzip_file
        )
        return data_ingestion