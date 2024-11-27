from Kidney_Disease.config.configuration import ConfigurationManager
from Kidney_Disease.components.mlflow_model_evaluation import Evaluation
from Kidney_Disease import logger
import distutils
import setuptools
import setuptools.dist

# Add version attribute to distutils
distutils.version = setuptools.__version__

STAGE_NAME="Model Evaluation"

class EvaluationPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()

if __name__=="__main__":
    try:
        logger.info("********************")
        logger.info(f"**{STAGE_NAME} has started**\n")
        model_eval_obj=EvaluationPipeline()
        model_eval_obj.main()
        logger.info(f"**{STAGE_NAME} has Ended **\n\nXXX===Model Evaluation Over=====XXX")

    except Exception as e:
        raise e    
