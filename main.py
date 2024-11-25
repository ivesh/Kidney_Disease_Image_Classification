from Kidney_Disease import logger
from Kidney_Disease.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from Kidney_Disease.pipeline.stage2_prepare_base_model import PrepareBasemodelTrainingPipeline


STAGE_NAME= "Data ingestion stage"

try:
    logger.info(f"Data ingestion main funtion has started and it is in stage:{STAGE_NAME}\n")
    pipeline=DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"Data ingestion main funtion has completed and it is in stage:{STAGE_NAME}\n")
except Exception as e:
    logger.exception (e)
    raise e
STAGE_NAME= "Prepare Base Model stage"

try:
    logger.info(f"Prepare base model main funtion has started and it is in stage:{STAGE_NAME}\n")
    base_model_pipeline=PrepareBasemodelTrainingPipeline()
    base_model_pipeline.main()
    logger.info(f"Prepare base model main funtion has completed and it is in stage:{STAGE_NAME}\n")
except Exception as e:
    logger.exception (e)
    raise e