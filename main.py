from text_summarization.logging import logger
from text_summarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


# 1st Stage

STAGE_NAME = "Data Ingestion Stage"
try:
   logger.info(f"####### {STAGE_NAME} has started #######") 
   objDITP = DataIngestionTrainingPipeline()
   objDITP.main()
   logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")

except Exception as e:
        logger.exception(e)
        raise e