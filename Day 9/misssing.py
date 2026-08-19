import pandas as pd
df=pd.read_csv("Employee.csv")
#print(df)
#print(df.isnull())
#print(df.isnull().sum())
#print(df.dropna())
#print(df[df.duplicated("Education")])
print(df.dtypes)
df["Age"]=df["Age"].astype(int)