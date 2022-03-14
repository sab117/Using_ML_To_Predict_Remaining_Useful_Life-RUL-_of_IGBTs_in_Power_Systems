#Last modified 04/02/2022
#By Saboor Rashid
#This code is seeing determining the time diffrence of the each frequency pulse 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_widths
##################################################################
df = pd.read_pickle("Set_1_Train_Data.pkl")
print(df)

#converted_df = pd.to_datetime(df['Epoch'],unit='D')
#print(converted_df)

Time_NA = df.iloc[:,0]
Time = Time_NA.values.flatten()
#print(Time)


Ic_NA = df.iloc[:,2]
Ic = Ic_NA.values.flatten() # Reshaping to a 1D array
#print(Ic)
#####################################################################

peaks, _ = find_peaks(Ic)
result = peak_widths(Ic,peaks,rel_height=1)
result[0]


result_half = peak_widths(Ic,peaks,rel_height=0.5)
result_half[0]
######################################################################

plt.plot(Ic)
plt.plot(peaks, Ic[peaks],'x')
plt.hlines(*result_half[1:], color="Green")
plt.hlines(*result[1:], color="Red")
plt.show()
#######################################################################

Result_1 = result
print(Result_1)

Data = Result_1

df2_NT = pd.DataFrame(Data)
df2 = df2_NT.T
print(df2)

#df2.to_excel('Data_Full.xlsx')

Result_2 = result_half
print(result_half)

Data_2 = Result_2

df3_NT = pd.DataFrame(Data_2)
df3 = df3_NT.T
print(df3)

df3.to_excel('Data_Half_Train.xlsx')





