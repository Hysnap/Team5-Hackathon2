import pandas as pd
import os

file_path = "/Users/saad/Documents/vscode-projects/Team5-Hackathon2/BankChurners.csv" 
df = pd.read_csv(file_path)

if df.isnull().sum().sum() > 0:
    print("Warning: Missing values detected. Consider handling them before analysis.")
    df.fillna(method='ffill', inplace=True)

duplicates = df[df.duplicated(subset=["CLIENTNUM"], keep=False)]
if not duplicates.empty:
    print("Warning: Duplicate CLIENTNUM entries detected. Consider removing them.")
    df.drop_duplicates(subset=["CLIENTNUM"], keep='first', inplace=True)

df["Attrition_Flag"] = df["Attrition_Flag"].map({"Existing Customer": 0, "Attrited Customer": 1})

df.to_csv("/Users/saad/Documents/vscode-projects/Team5-Hackathon2/BankChurners.csv", index=False)

print("ETL process completed. Cleaned data saved as 'Cleaned_BankChurners.csv'.")

# 3. Identify and Impute Categorical Columns
categorical_cols = [
    'Attrition_Flag',
    'Gender',
    'Education_Level',
    'Marital_Status',
    'Income_Category',
    'Card_Category'
]

for col in categorical_cols:
    if df[col].isnull().any():
        most_frequent_value = df[col].mode()[0]
        df[col] = df[col].fillna(most_frequent_value)

# 4. One-Hot Encoding
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore', drop=None)
encoded_data = encoder.fit_transform(df[categorical_cols])
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_cols), index=df.index)

# 5. Concatenate and Display
df2 = pd.concat([df, encoded_df], axis=1)
print df2.head