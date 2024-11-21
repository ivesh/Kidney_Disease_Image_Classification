from Kidney_Disease.config.configuration import ConfigurationManager
from Kidney_Disease.components.data_ingestion import DataIngestion
from Kidney_Disease import logger

STAGE_NAME= "Data ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            logger.info(f"Error occurred in data ingestion stage: {str(e)}")
            raise e
        
if __name__=='__main__':
    try:
        logger.info(f"Data ingestion main funtion has started and it is in stage:{STAGE_NAME}")
        pipeline=DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f"Data ingestion main funtion has completed and it is in stage:{STAGE_NAME}")
    except Exception as e:
        logger.exception (e)
        raise e
    
