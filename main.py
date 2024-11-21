from Kidney_Disease import logger
logger.info("Logging successul for from Kidney_Disease import logger instead of  from src.Kidney_Disease import logger. The setup.py file is congigured to src not Kidney_Disease.")
from Kidney_Disease.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME= "Data ingestion stage"

try:
    logger.info(f"Data ingestion main funtion has started and it is in stage:{STAGE_NAME}")
    pipeline=DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"Data ingestion main funtion has completed and it is in stage:{STAGE_NAME}")
except Exception as e:
    logger.exception (e)
    raise e