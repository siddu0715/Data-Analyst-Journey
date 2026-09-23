import pandas as pd
df=pd.read_csv("Employee.csv")
#print(df.isnull().sum())
#print(df.dropna())
#print(df.fillna(0))
#print(df.duplicated())
#print(df.drop_duplicates())
#print(df.astype({"Salary": "int"}))
print(df.value_counts())