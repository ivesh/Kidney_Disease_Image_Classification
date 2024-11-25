from Kidney_Disease.config.configuration import ConfigurationManager
from Kidney_Disease.components.prepare_base_model import PrepareBaseModel
from Kidney_Disease import logger

STAGE_NAME="Prepare Base Model"

class PrepareBasemodelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e

if  __name__=="__main__":
    try:
        logger.info(f"*********")
        logger.info(f"*********{STAGE_NAME} has started********\n")
        base_model_obj=PrepareBasemodelTrainingPipeline()
        base_model_obj.main()
        logger.info(f"*********{STAGE_NAME} has completed******** \n")
    except Exception as e:
            raise e        