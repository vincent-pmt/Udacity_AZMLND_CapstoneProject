from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

def clean_data(data):
    # Clean and one hot encode data
    x_df = data
    y_df = data.pop("DEATH_EVENT")
    return x_df, y_df

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run = Run.get_context()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    # TODO: Create TabularDataset using TabularDatasetFactory
    # Data is located at: https://storage.googleapis.com/kagglesdsdata/datasets/727551/1263738/heart_failure_clinical_records_dataset.csv
    # Uploaded to local blogstorage

    datapath = "https://udcmachinelear1853326931.blob.core.windows.net/sharedfile/heart_failure_clinical_records_dataset.csv"
    ds = TabularDatasetFactory.from_delimited_files(path=datapath)
    data_df = ds.to_pandas_dataframe()

    print(data_df)

    x, y = clean_data(data_df)

    # TODO: Split data into train and test sets.
 
    # split the dataset
    x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.05, random_state=0)

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()


