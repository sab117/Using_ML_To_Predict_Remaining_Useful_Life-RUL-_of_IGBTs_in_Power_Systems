#Last Modified 11/02/2022
#By Saboor Rashid
#This produces a graph that shows the the current vs
# Time diffrence to get cluster to with there centroids of 
# collector current 
# to be used to predict the RUL of this IGBT
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn.cluster as cluster
import sklearn.cluster as Kmeans


df1 = pd.read_pickle('Full_Set_Cluster')
#print(df1)

Td1 = df1.iloc[:,0]
#print(Td1)

Ic1 = df1.iloc[:,1]
#print(Ic1)


Data_train = [Td1,Ic1]
df2_NT = pd.DataFrame(Data_train)
df2=df2_NT.T
#print(df2)

arr_Full = df2.to_numpy()
#print(arr_Full)

##################################################

#Technically 3 clusters but using 4 gives a more clearer image
km = cluster.KMeans(n_clusters=4)
y_km = km.fit_predict(arr_Full)

center = km.cluster_centers_

print(center)
#print(y_km)
####################################################



Label_0= arr_Full[y_km == 0]

Label_1 = arr_Full[y_km == 1]

Label_2 = arr_Full[y_km == 2]

Label_3 = arr_Full[y_km == 3]




plt.scatter(Label_0[:,0], Label_0[:,1],color ='red')
plt.scatter(Label_1[:,0], Label_1[:,1],color ='blue')
plt.scatter(Label_2[:,0], Label_2[:,1],color ='green')
plt.scatter(Label_3[:,0], Label_3[:,1],color ='orange')


plt.scatter(center[:,0], center[:,1],c='black')
plt.xlabel('Time Difference TD (Epoch)')
plt.ylabel('Collector Current Ic (A)')
plt.title('K-Means Cluster Model')
plt.grid()

plt.show()