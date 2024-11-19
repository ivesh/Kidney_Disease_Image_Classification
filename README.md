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

1. Update config.yaml
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
            The functionality of configbox and ensure annotations are demonstrated in trials.ipynb file    
-    
