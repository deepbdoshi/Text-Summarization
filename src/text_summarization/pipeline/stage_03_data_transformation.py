from text_summarization.config.configuration import ConfigurationManager
from text_summarization.components.data_transformation import DataTransformation
from text_summarization.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        logger.info("Setting Config Object...")
        config = ConfigurationManager()
        
        logger.info("Reading configs...")
        data_transformation_config = config.get_data_transformation_config()
        
        logger.info("Data Transforming Object...")
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()