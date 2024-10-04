from text_summarization.config.configuration import ConfigurationManager
from text_summarization.components.data_ingestion import DataIngestion
from text_summarization.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        "Currently nothing to initialize"
        pass

    def main(self):
        """
        Data Ingestion Pipeline - Gets the Configuration Manager Object to create the config object.
                                  This object is then used to download the data in the configured path.
        """
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

        except Exception as e:
            raise e

