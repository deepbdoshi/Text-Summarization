from text_summarization.config.configuration import ConfigurationManager
from text_summarization.components.data_validation import DataValiadtion
from text_summarization.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        """
        Data Validation Pipeline - Gets the Configuration Manager Object to create the config object.
                                  This object is then used to perform the data validation checks on the ingested data.
        """
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()