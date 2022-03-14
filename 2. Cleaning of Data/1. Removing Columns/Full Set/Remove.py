#Last modified 03/02/2022
#By Saboor Rashid
#This code is simply removing the unwanted columns 

import pandas as pd



df = pd.read_pickle("Full_Set")
print(df)
print(df.info())

del df["Heat Sink Temp"]
del df["Unnamed: 4"]
del df["Unnamed: 7"]
del df["Unnamed: 10"]
del df["Unnamed: 12"]
del df["Unnamed: 14"]

print(df)

df.to_pickle('Full_Set_Clean')