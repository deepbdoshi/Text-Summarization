from text_summarization.logging import logger
from text_summarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarization.pipeline.stage_02_data_validation import DataValidationTrainingPipeline


# 1st Stage

# STAGE_NAME = "Data Ingestion Stage"
# try:
#    logger.info(f"####### {STAGE_NAME} has started #######") 
#    objDITP = DataIngestionTrainingPipeline()
#    objDITP.main()
#    logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")

# except Exception as e:
#         logger.exception(e)
#         raise e


# 2nd Stage

STAGE_NAME = "Data Validation Stage"
try:
   logger.info(f"####### {STAGE_NAME} has started #######")
   objDVTP = DataValidationTrainingPipeline()
   objDVTP.main()
   logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")
except Exception as e:
        logger.exception(e)
        raise e