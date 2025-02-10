import numpy as np
import pandas as pd
open ("BankChurners.csv")
df = pd.read_csv("BankChurners.csv")
df.describe()
df['CLIENTNUM'].is_unique
df.isnull().sum()
df.info()
df = pd.read_csv("BankChurners.csv")
df_categorical = df[['Attrition_Flag', 'Gender', 'Education_Level', 'Marital_Status', 'Income_Category', 'Card_Category']]
df_categorical.info()
df_categorical.head()
def load_and_process_data("BankChurners.csv"):
    df = pd.read_csv("BankChurners.csv")
    df["Attrition_Flag_Encoded"] = df["Attrition_Flag"].map({"Existing Customer": 1, "Attrited Customer": 0})
    df["Gender_Encoded"] = df["Gender"].map({"M": 2, "F": 3})
    df["Education_Level_Encoded"] = df["Education_Level"].astype('category').cat.codes / 10
    df["Marital_Status_Encoded"] = df["Marital_Status"].astype('category').cat.codes
    df["Income_Category_Encoded"] = df["Income_Category"].str.extract(r'(\d+)').astype(float).fillna(0).astype(int)
    df["Card_Category_Encoded"] = df["Card_Category"].astype('category').cat.codes * 10

    return df
file_path = "BankChurners_Cleaned_Encoded.csv" 
df_processed = load_and_process_data(file_path)
print(df_processed.head())