# 🧠 Kidney Disease Classification (CT Scan)

## 1. Project Objective

* **Goal**: Build an **end-to-end deep learning pipeline** that classifies kidney CT scans into:

  * **Normal**
  * **Cyst**
  * **Tumor**
  * **Stone**
* **Key Features**:

  * Modular coding with OOP (classes & functions)
  * Reproducible pipelines with **DVC**
  * Experiment tracking with **MLflow**
  * Deployment with **Flask API + Docker + CI/CD on AWS**

---

## 2. Project Dependencies

Dependencies are listed in **`requirements.txt`**:

* `tensorflow==2.12.0` → deep learning model training
* `pandas`, `numpy` → data manipulation
* `matplotlib`, `seaborn` → visualization
* `mlflow==2.2.2` → experiment tracking
* `dvc` → data version control and pipeline orchestration
* `Flask`, `Flask-Cors` → deployment API
* `tqdm` → progress bar
* `python-box`, `pyyaml`, `types-PyYAML` → config management
* `joblib`, `scipy` → utility support
* `gdown` → dataset download from Google Drive
* `-e .` → install local package (`src/` as a module)

Install via:

```bash
pip install -r requirements.txt
```

---

## 3. File Structure

```
KIDNEY-DISEASE-CLASSIFICATION/
│── config/
│   └── config.yaml        # central config file
│
│── research/
│   └── trials.ipynb       # notebook experiments
│
│── src/cnnClassifier/
│   │── __init__.py
│   │── components/        # modular pipeline components
│   │── config/            # configuration manager
│   │── constants/         # project-wide constants
│   │── entity/            # dataclasses for configs
│   │── pipeline/          # training & prediction pipelines
│   │── utils/             # logging, helper functions
│
│── templates/
│   └── index.html         # frontend for Flask app
│
│── dvc.yaml               # DVC pipeline definition
│── params.yaml            # training hyperparameters
│── requirements.txt       # dependencies
│── setup.py               # installable package
│── template.py            # auto-generates folder structure
│── README.md              # project documentation
```

---

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

## 4. Explanation of Files & Workflow

### 🔹 Step 1: Setup & Initialization

* **`template.py`**

  * Auto-generates folder structure (`src/`, `config/`, etc.)
  * Uses `os` + `logging` for structured creation
  * First file executed to set up repo

* **`setup.py`**

  * Installs `src/` as a local package (`-e .`)
  * Required for imports like:

    ```python
    from cnnClassifier.pipeline import training_pipeline
    ```

---

### 🔹 Step 2: Config & Parameters

* **`config/config.yaml`**

  * Stores dataset paths, artifact directories, model paths.
* **`params.yaml`**

  * Stores hyperparameters:

    * `IMG_SIZE`, `BATCH_SIZE`, `EPOCHS`, `LEARNING_RATE`, etc.
* **`src/cnnClassifier/constants`**

  * Defines constant values to be used across project.
* **`src/cnnClassifier/entity`**

  * Contains dataclasses (entities) to strongly type config sections.

---

### 🔹 Step 3: Utilities

* **`src/cnnClassifier/utils/__init__.py`**

  * Logging setup:

    ```python
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    ```
  * File + console logging
* Utility functions: path handling, yaml reading/writing, save/load models

---

### 🔹 Step 4: Components

Each component is a **class-based module**:

* `data_ingestion.py` → downloads & extracts dataset (`gdown`, unzip)
* `prepare_base_model.py` → loads pre-trained CNN (e.g., VGG16, ResNet)
* `model_trainer.py` → trains transfer learning model
* `model_evaluation.py` → evaluates accuracy, logs metrics with MLflow

---

### 🔹 Step 5: Pipelines

* **`src/cnnClassifier/pipeline/training_pipeline.py`**

  * Orchestrates all components:

    1. Data Ingestion
    2. Base Model Preparation
    3. Training
    4. Evaluation
* **`src/cnnClassifier/pipeline/prediction_pipeline.py`**

  * Loads trained `.h5` model
  * Accepts input CT scan
  * Outputs prediction (`Normal`, `Tumor`, etc.)

---

### 🔹 Step 6: Flask App

* **`app.py`**

  * Flask web service with routes:

    * `/train` → triggers training pipeline
    * `/predict` → takes uploaded CT scan → returns class
  * Uses **templates/index.html** for UI

Run:

```bash
python app.py
```

Open browser: `http://127.0.0.1:8080`

---

### 🔹 Step 7: DVC & MLflow

* **`dvc.yaml`**

  * Defines pipeline stages:

    ```yaml
    stages:
      data_ingestion:
        cmd: python src/cnnClassifier/components/data_ingestion.py
        outs: [artifacts/data]
      prepare_base_model:
        cmd: python src/cnnClassifier/components/prepare_base_model.py
      training:
        cmd: python src/cnnClassifier/components/model_trainer.py
      evaluation:
        cmd: python src/cnnClassifier/components/model_evaluation.py
    ```
* **Run pipeline**:

  ```bash
  dvc repro
  ```
* **Track experiments**:

  ```bash
  mlflow ui
  ```

  Open: `http://127.0.0.1:5000`

---

### 🔹 Step 8: CI/CD & Deployment

1. **Dockerfile**

   * Containerize Flask app + model

   ```dockerfile
   FROM python:3.8
   COPY . /app
   WORKDIR /app
   RUN pip install -r requirements.txt
   CMD ["python", "app.py"]
   ```

2. **GitHub Actions** (`.github/workflows/main.yml`)

   * Build Docker image
   * Push to AWS ECR / DockerHub
   * Deploy on AWS EC2/ECS

3. **Deployment Steps**

   ```bash
   docker build -t kidney-classifier .
   docker run -p 8080:8080 kidney-classifier
   ```

   Access via `http://<EC2-IP>:8080`

---

## 5. Execution Order (Chronological)

1. `template.py` → create folder structure
2. `setup.py` → install local package
3. `config/config.yaml` + `params.yaml` → define config
4. `entity/` → define dataclasses
5. `components/` (data\_ingestion → base\_model → training → evaluation)
6. `pipeline/training_pipeline.py` → orchestrates components
7. `pipeline/prediction_pipeline.py` → for predictions
8. `dvc.yaml` → reproducible pipeline execution
9. `mlflow` → log experiments
10. `app.py` → Flask app
11. `Dockerfile` + CI/CD workflow → Deployment on AWS

---

## 6. Fetching Results

* Run locally:

  ```bash
  python app.py
  ```
* Upload CT scan → get predicted class
* Or run prediction pipeline directly:

  ```bash
  python src/cnnClassifier/pipeline/prediction_pipeline.py --image test.png
  ```

---

## 7. Project Lifecycle

1. **Problem Definition** → Classify kidney CT scans (Normal, Cyst, Tumor, Stone)
2. **Data Ingestion** → Download dataset from Kaggle/Drive
3. **Data Preprocessing** → Augmentation, resizing, normalization
4. **Model Preparation** → Transfer Learning (VGG16/ResNet)
5. **Training & Evaluation** → MLflow tracking, DVC pipeline
6. **Packaging** → `setup.py`, modular coding
7. **Deployment** → Flask API + Docker + CI/CD on AWS
8. **Monitoring** → Logs, MLflow experiments, retraining on new data

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
---


     
