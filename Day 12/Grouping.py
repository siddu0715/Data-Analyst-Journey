import pandas as pd
df=pd.read_csv("Employee.csv")
#print(df)
#print(df.groupby(["Department", "City"])["Salary"].mean())
#print(df.groupby(["Department", "City"])["Salary"].agg(["mean", "sum", "count"]))
print(df.groupby("Department")["Salary"].agg([("Average Salary", "mean"), ("Total Salary", "sum"), ("Employee Count", "count")]))