from Kidney_Disease import logger
from Kidney_Disease.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from Kidney_Disease.pipeline.stage2_prepare_base_model import PrepareBasemodelTrainingPipeline
from Kidney_Disease.pipeline.stage3_model_training import ModelTrainingPipeline




STAGE_NAME= "Data ingestion stage"

try:
    logger.info(f"Data ingestion main funtion has started and it is in stage:{STAGE_NAME}\n")
    pipeline=DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"Data ingestion main funtion has completed and it is in stage:{STAGE_NAME}\n \n\n x=====End of the stage=====x")
except Exception as e:
    logger.exception (e)
    raise e
STAGE_NAME= "Prepare Base Model stage"

try:
    logger.info(f"Prepare base model main funtion has started and it is in stage:{STAGE_NAME}\n")
    base_model_pipeline=PrepareBasemodelTrainingPipeline()
    base_model_pipeline.main()
    logger.info(f"Prepare base model main funtion has completed and it is in stage:{STAGE_NAME}\n \n\n x=====End of the stage=====x")
except Exception as e:
    logger.exception (e)
    raise e
STAGE_NAME= "Model Training stage"
try:
    logger.info(f"Prepare base model main funtion has started and it is in stage:{STAGE_NAME}\n")
    model_training_pipeline=ModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info(f"Prepare base model main funtion has completed and it is in stage:{STAGE_NAME}\n \n\n x=====End of the stage=====x")
except Exception as e:
    logger.exception (e)
    raise e