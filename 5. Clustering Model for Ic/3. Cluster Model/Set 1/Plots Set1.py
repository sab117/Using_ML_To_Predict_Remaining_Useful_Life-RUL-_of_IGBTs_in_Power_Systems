#Last Modified 06/02/2022
#By Saboor Rashid
#Visualisng the set data with training and testing data 
import matplotlib.pyplot as plt
import pandas as pd



df1 = pd.read_pickle('FSet_1_Train')
df2 = pd.read_pickle('FSet_1_Testing')

print(df1)
print(df2)

Td1 = df1.iloc[:,0]
print(Td1)

Ic1 = df1.iloc[:,1]
print(Ic1)

Td2 = df2.iloc[:,0]
print(Td2)

Ic2 = df2.iloc[:,1]
print(Ic2)

plt.scatter(x=Td1,y=Ic1)
plt.scatter(x=Td2,y= Ic2)
plt.xlabel("Time Difference TD (Epoch Time)")
plt.ylabel("Collector Current Ic (A)")
plt.show()


