# Udacity Capstone Project - Azure ML Engineer - Heart failure prediction

The objective of the project was to utilize Azure's AutoML and Hyperdrive capabilities to train various models, identify the most efficient one, and then deploy it as a web service. The final step involved evaluating the service's endpoints to determine individuals at elevated risk of cardiovascular issues, which could be due to multiple risk factors including high blood pressure, diabetes or pre-existing conditions. This approach aimed to streamline the prediction process for high-risk cardiovascular conditions.

## Project Set Up and Installation
The dataset has been downloaded from Kaggle and manually upload to Blogstorrage.

## Dataset

### Overview
The heart_failure_clinical_records_dataset.cvs was acquired from Kaggle (Dataset from Davide Chicco, Giuseppe Jurman). 
https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data/data

About the data
age: Age of the patient
anaemia: Haemoglobin level of patient (Boolean)
creatinine_phosphokinase: Level of the CPK enzyme in the blood (mcg/L)
diabetes: If the patient has diabetes (Boolean)
ejection_fraction: Percentage of blood leaving the heart at each contraction
high_blood_pressure: If the patient has hypertension (Boolean)
platelets: Platelet count of blood (kiloplatelets/mL)
serum_creatinine: Level of serum creatinine in the blood (mg/dL)
serum_sodium: Level of serum sodium in the blood (mEq/L)
sex: Sex of the patient
smoking: If the patient smokes or not (Boolean)
time: Follow-up period (days)
DEATH_EVENT: If the patient deceased during the follow-up period (Boolean)

### Task
The task is to determine whether a patient passed away during the follow-up period. For this purpose, we will utilize the 'DEATH_EVENT' column as our target variable. Given that 'DEATH_EVENT' is a boolean variable, indicating only two possible outcomes, our analysis falls under the category of Binary Classification. 

### Access
Open the Azure AI | Machine Learning Studio, navigate to the 'Data' section and establish a fresh dataset by uploading a CSV file from the local machine.
![Heart Failure Dataset](/images/dataset.jpeg)
![Dataset](/images/dataset_view.jpeg)

## Automated ML
### An overview of the `automl` settings and configuration
Create a cluster instance
![Cluster](/images/cluster.jpeg)

the compute target that we provisioned is set with compute_target=cluster, and the number of max_concurrent_iterations of your experiment should be matched to the number of nodes in the cluster.
The argument task is set to classification since we are dealing with a binary classification and we also need to set label_column_name="DEATH_EVENT" in order to predicting DEATH_EVENT. 
The dataset should be specified in training_data=dataset.
set "primary_metric" : 'accuracy' to select the best model by Using accuracy metrix

![AutoML Configuration](/images/AutoMLConfig.jpeg)

### Results

The best performing model trained by AutoML was VotingEnsemble with Accuracy 0.88638

#### `RunDetails` widget as well as a screenshot of .
![RunDetails witdet](/images/RunDetails_widget.jpeg)

#### the best model trained with it's parameters

![AutoML Best Model](/images/AutoML_bestmodel.jpeg)

![Submit Experience](/images/Experience_Submit.jpeg)

#### Save the best model 

![Save AutoML bestmodel](/images/AutoML_SaveBestModel.jpeg)

#### Register The best Model
![Register Model](/images/AutoML_RegisterModel.jpeg)

![Experience Best Model](/images/Experience_BestModel.jpeg)

## Hyperparameter Tuning

I'm using The Scikit-learn Logistic Regression, Scikit-learn plays a significant role in simplifying the implementation of logistic regression.
I've opted for a approach with the random selection for its two parameters. This means that the values of the parameters were not predetermined, but randomly. 
Random sampling is straightforward to implement. No complex algorithms or heuristics are needed. It’s a good starting point for hyperparameter tuning, especially when little prior knowledge about the problem exists.

![Hyperparameter Configuration](/images/Hyper_config.jpeg)

 Random parameters:
 - --C - Inverse of regularization strength (default: 1.0)
 - --max_iter - Maximum number of iterations convergence (default: 100)

### Results

The accuracy of the best model given by HyperDrive is 0.8 with 
    Regularization Strength: 5
    Max iterations: 200

#### the screenshots of the RunDetails widget

![Hyperparameter RunDetails](/images/Hyper_Rundetails.jpeg)

![Hyperparameter Run Completed](/images/Hyper_RunCompleted.jpeg)

#### the best model trained with it's parameters

![Hyperparameter Best Model](/images/Hyper_BestModel.jpeg)

![Hyperparameter Best Model with Parameters](/images/Hyper_BestModel_Para.jpeg)

#### Improvement:

- Training a new model by using a dataset with more data.
- Try with more Parameter Sampling
- try different classification methods like SVMs and trees
- Optimise on the training set and use the test set as an object evaluation of the method

## Model Deployment

The accuracy scores are close, with the autoML pipeline (accuracy: 0.88638) outperforming the scikit-learn pipeline (accuracy: 0.8) by 0.086 points.

So I deploy the best model from AutoML experiment and using Azure Container Instance.

![Deploy Best Model](/images/AutoML_DeployBestModel.jpeg)

#### Endpoint Details 

![AutoML Model Endpoint](/images/AutoML_BestModel_Endpoint.jpeg)

#### Endpoint Status 

![Endpoint Status](/images/Endpoint_Status.jpeg)

#### Service Log 

![Service Log](/images/Service_Log.jpeg)

#### 'TESTING' query the endpoint with a sample input.

In order to perform a prediction, we need to get the Rest endpoint and the authentication key if it's required.

Prepare a sample dataset and convert it to JSON format before injecting it into the request for evaluation.

![Endpoint URI](/images/Endpoint_URI_Code.jpeg)

Should get the result if the input data and header are invalid.

![Endpoint Request](/images/Endpoint_Request_Result.jpeg)

## Screen Recording
The screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

Please click here for viewing. (Please enable the caption on this video)

[![Watch the video](https://i9.ytimg.com/vi_webp/p8kM4h0HFyo/mq3.webp?sqp=CIzT4rAG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGBMgTyh_MA8=&rs=AOn4CLBTCxdvN70H7pj0GBu-nkRcMcAVVA)](https://youtu.be/p8kM4h0HFyo)

## Future work/improvement
- Increasing the number of clusters used to speed up the analysis. These steps could help to reduce the error in our model and study it more efficiently.
- Implement a load test for the model's endpoint, such as simulating high traffic to the endpoint and measuring its responsiveness.