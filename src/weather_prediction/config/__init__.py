from weather_prediction.entity import *
from weather_prediction.constants import *
from weather_prediction.utils import *


class ConfigurationManager:

    def __init__(self, config = config, params = params, schema = schema):
        self.config = read_yaml(config)
        self.params = read_yaml(params)
        self.schema = read_yaml(schema)

        create_dir([self.config.root])