from textSummarizer.pipeline.stage1_dataIngestion import DataIngestionTrainingPipeline 
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
