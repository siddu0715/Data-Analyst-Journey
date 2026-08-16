import pandas as pd
import numpy as np
data={
    "name": ["siddu","dp","bala","prabha","kiran"],
    "age":[19,20,19,22,21],
    "marks":[88,98,77,55,69]
    }
df=pd.DataFrame(data)
#print(df)
print(df[df["marks"]>=70])
print(df[df["name"] == "siddu"])
print(df[(df["age"]>20) & (df["marks"]>80)])