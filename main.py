from text_summarization.logging import logger
from text_summarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summarization.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from text_summarization.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from text_summarization.pipeline.stage_04_model_training import ModelTrainingPipeline
from text_summarization.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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

# STAGE_NAME = "Data Validation Stage"
# try:
#    logger.info(f"####### {STAGE_NAME} has started #######")
#    objDVTP = DataValidationTrainingPipeline()
#    objDVTP.main()
#    logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")
# except Exception as e:
#         logger.exception(e)
#         raise e


# 3rd Stage

# STAGE_NAME = "Data Transformation Stage"
# try:
#    logger.info(f"####### {STAGE_NAME} has started #######")
#    objDTTP = DataTransformationTrainingPipeline()
#    objDTTP.main()
#    logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")
# except Exception as e:
#         logger.exception(e)
#         raise e


# 4th Stage

# STAGE_NAME = "Model Training Stage"
# try:
#    logger.info(f"####### {STAGE_NAME} has started #######")
#    objMTP = ModelTrainingPipeline()
#    objMTP.main()
#    logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")
# except Exception as e:
#         logger.exception(e)
#         raise e

# 5th Stage

STAGE_NAME = "Model Evaluation Stage"
try: 
   logger.info(f"####### {STAGE_NAME} has started #######")
   objME = ModelEvaluationTrainingPipeline()
   objME.main()
   logger.info(f"####### {STAGE_NAME} is completed #######\n\n\n")
except Exception as e:
        logger.exception(e)
        raise e