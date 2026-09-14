import pandas as pd
df=pd.read_csv("Employee.csv")
#print(df)
#print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department").agg({
    "Salary": ["mean", "max"],
    "Age": ["mean","max"]
}))