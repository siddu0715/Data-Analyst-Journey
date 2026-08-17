import pandas as pd
import numpy as np
data={
    "name":["siddu","bala","kiran","dp","prabha"],
    "age":[19,20,21,22,23],
    "department":["cse","csd","ece","civil","mech"],
    "marks":[90,80,70,60,50]
}
df=pd.DataFrame(data)
#print(df)
df["grade"]=["A","B","C","D","E"]
df["marks"]=df["marks"]+5
df=df.rename(columns={"marks":"score"})
df.drop("age",axis=1)
print(df)
print(df[df["score"]>80])