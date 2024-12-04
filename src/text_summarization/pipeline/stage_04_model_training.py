from text_summarization.config.configuration import ConfigurationManager
from text_summarization.components.model_training import ModelTraining
from text_summarization.logging import logger


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_training_config()
        model_trainer_config = ModelTraining(config=model_trainer_config)
        model_trainer_config.train()