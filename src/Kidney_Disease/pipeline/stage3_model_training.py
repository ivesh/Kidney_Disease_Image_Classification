from Kidney_Disease.config.configuration import ConfigurationManager
from Kidney_Disease.components.model_training import Training
from Kidney_Disease import logger

STAGE_NAME = "Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__=="__main__":
    try:
        logger.info(f"**************** \n")
        logger.info(f"The stage: {STAGE_NAME} has started \n")
        training_model_obj= ModelTrainingPipeline()
        training_model_obj.main()
        logger.info(f"**************** \n\n x=====End of the stage=====x")
    except Exception as e:
        raise e        