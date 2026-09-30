import pandas as pd
df = pd.read_csv("Employee.csv")
df.max("Salary")