from textSummarizer.pipeline.stage1_dataIngestion import DataIngestionTrainingPipeline 
from textSummarizer.pipeline.stage2_dataValidation import DataValidationTrainingPipeline 
from textSummarizer.pipeline.stage3_dataTransformation import DataTransformationTrainingPipeline 
from textSummarizer.logging import logger 

STAGE_NAME = 'Data Ingestion Stage' 

try:
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<')
    data_ingestion = DataIngestionTrainingPipeline() 
    data_ingestion.main()
    logger.info(f'>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<<') 
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Validation Stage' 

try:
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<')
    data_validation = DataValidationTrainingPipeline() 
    data_validation.main()
    logger.info(f'>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<<') 
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation Stage' 

try:
    logger.info(f'>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<')
    data_transformation = DataTransformationTrainingPipeline() 
    data_transformation.main()
    logger.info(f'>>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<<<<') 
except Exception as e:
    logger.exception(e)
    raise e
