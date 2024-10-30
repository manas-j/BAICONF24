# utils/data_processing.py

import pandas as pd
from sklearn.impute import SimpleImputer

def load_and_process_data(file_path, esg_columns, financial_columns):
    """Load and preprocess the dataset."""
    data = pd.read_csv(file_path)
    # Select relevant columns
    data_numeric = data[esg_columns + financial_columns]
    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    data_imputed = pd.DataFrame(imputer.fit_transform(data_numeric), columns=data_numeric.columns)
    return data_imputed
