# hate-speech-end-to-end-project


- Git clone the repository and define the template of the project
```bash
git clone https://github.com/-----
touch template.py
python template.py
```

- define setup.py file

- install the new env and requirements.txt
```bash
conda create -n nlp-project python=3.10 -y
conda activate nlp-project
pip install -r requirements.txt
```

- define the logger
- define the exception handler

- Get the dataset and store in AWS S3 bucket
- Run the experiments.ipynb notebook in google colab and try different models
    - EDA
    - Feature Engineering
    - Model 0: Naive Bayes (baseline)
    - Model 1: A simple dense model
    - Model 2: LSTM
    - Model 3: GRU
    - Model 4: Bidirectonal RNN model
    - Model 5: Conv1D
    - Model 6: TensorFlow Hub Pretrained Sentence Encoder
    - Model 7: LSTM (second method)

```bash
## Workflows

- update the constants
- updata the artifact_entity
- update the config_entity
- update the components
- update the pipeline
- update the dvc.yaml
```

- **Data Ingestion**
    - add s3_operations.py for uploading and downloading files from s3 bucket 
    - we need to run the below command which allows to configure AWS credentials and settings 
    ```bash
    aws configure
    ```
    - follow the above workflows to get the data from the S3 bucket