import pandas as pd
import numpy as np
data={
    "name": ["siddu","dp","bala","prabha","kiran"],
    "roll no":[62,50,47,59,54],
    "marks":[88,98,77,np.nan,69]
    }
df=pd.DataFrame(data)
#print(df)
#print(df.head())
#print(df.count())
#print(df.describe())
#print(df['marks'].mean())
# Get the row(s) with the maximum marks
#print(df[df["marks"] == df["marks"].max()])
print(df[df["marks"] == df["marks"].min()])
#filling null with 0
df['marks'].fillna(0, inplace=True)
print(df['marks'].fillna(0, inplace=True))
