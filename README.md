# Kidney disease Classification

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```
## Goals of the project to classify Kidney disease as per the images if it is normal or not.

## Workflows

1. Update config.yaml- Data ingestion and certain config will be used.
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py


## File Structure
Kidney_Disease Folder:
    __init__.py: Logger code is kept here instead od creating an other one to directly import the logger file without mentioning src.Kidney_Disease the same setup has been done under setup.py.

    Utils Folder:
        -common.py : all commonly used functions used throughout the project is stored here. 
            This file has the following functions. On top of every function ensure annotation decorator is used to make sure the output and the input behave exactly as it is coded.
                1. Read yaml and return configbox return type
                2. Create directories for artifacts folder, data ingestion and data validation
                3. save_json is used to save the model metrics
                4. load_bin is used to load the binary file
                5. get_size is used to get the size of a file
                6. decodeImage
                7. encodeImage is used to when building prediction pipeline and user app. 
            The functionality of configbox and ensure annotations are demonstrated in trials.ipynb file along with gdown module to download link from google drive to test the data and be able to fetch the data.   
-   Data Ingestion workflow: The necessary code snippet has been successfully tried in the 01_data_ingestion.ipynb notebook file.
    config.yaml- the artifacts folder structure where our images needs to be downloaded from, the file directory it needs to be saved is mentioned. The important attributes are:
        - artifacts_root: artifacts
        - data ingestion: 
            - root_dir: "directory within which the data should be stored locally"
            - data_source_url: "the path where the images are downloaded from"
            - local_data_file: "file name and the directory where downloaded data will be stored"
            - unzip_dir: "directory where the unzipped content will reside"
    params.yaml- A dummy value has been assigned at this point of time with a basic key:val pair else it would give an error later while executing.
    entity folder- It will consist of a file config_entity.py which contains the configuration for data ingestion using dataclass and the parameters set to frozen.
        config_entity.py- The data ingestion configuration is defined here. The data ingestion configuration is defined here
    constants folder- It will contain the code where the path of our directories is fixed which is CONFIG_FILE_PAATH AND PARAMS_FILE_PATH. 
    config folder- It will consist of a file named configuration.py which will contain the configuration manager.   
        configuration.py- One of the function is used to create directories and the other is used to set the get_data_ingestion_config to data ingestion config set in entity.
    COMPONENTS folder: It will consist of a data_ingestion.py file.
        data_ingestion.py- This file will be having a class DataIngestion which will have two main methods which are download data from gdrive and extract all files to Unzip_directory   
    Pipeline Folder: It is structured in different stages where for the first stage stage1_data_ingestion.py file is prepared to handle data ingestion.
        stage1_data_ingestion.py- This file will be having a class DataIngestionPipeline class where config is set to configuration manager, data_ingestion_config is set to get_data_ingestion method, data_ingestion variable is initialized to DataIngestion class within which config is set to data_ingestion_config. After this data_ingestion.download_file() and  data_ingestion.extract_files() has been executed.
        if __name__==__main__ is used to run the class DataIngestionPipeline.
    main.py file: it will import data ingestion pipeline which will be initialized to a variable that can be used to run the main code present within DataIngestionPipeline class to download and extract our data.     

- Prepare base model workflow: The necessary code snippet has been successfully tried in the 02_prepare_base_model.ipynb and the same will be arranged as per the workflow. A base model will be dowloaded from Keras application in this case it is VGG16 with custom layers using Softmax activation function. VGG16 will have CNN layers as well as FC layer containing ANN. We will be using CNN layer along with custom FC layer.
    config.yaml- the prepare base model file structure is updated which contains root dir, base models directory saved as .h5 file, and updated base model directory. 
    params.yaml- A dummy value has been assigned at this point of time with a basic key.
