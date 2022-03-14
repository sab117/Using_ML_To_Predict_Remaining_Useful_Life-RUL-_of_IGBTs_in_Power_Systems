#Last modified 03/02/2022
#By Saboor Rashid
#This code is simply removing the unwanted columns 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_pickle("Set_4")
print(df)
#print(df.info())

del df["Heat Sink Temp"]
del df["Unnamed: 4"]
del df["Unnamed: 7"]
del df["Unnamed: 10"]
del df["Unnamed: 12"]
del df["Unnamed: 14"]

print(df)

df.to_pickle('Set_4_Clean')