#Last modified 09/03/2022
#By Saboor Rashid
#Plottig the ML model LR lines with cluster centroids to get timestamp of where to start the RUL countdown
#Timestamps are achived by visual inpection
#Added title



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Reading and getting the data into python into a format to work with
df = pd.read_pickle("Full_Set_Clean")
#print(df)

Epoch = df.iloc[:,0]
#print(Epoch)

Ic = df.iloc[:,3]
#print(Ic)



x_values = np.array(Epoch)
#print(x_values)


###########################################
#ML LR model equation of lines

y_1 = -9.97891076*x_values + 635407.54605372

y_2 = 13.99073561*x_values - 890852.93749685

y_3 = 25.18149833*x_values - 1603422.45016536

y_4 = 7.70682476*x_values - 490725.84552345

#Centroids from Cluster model
y_c1 = 3.99467477

y_c2 = 4.12247406

y_c3 = 4.07079973

########################################################
#Plotting the lines with centroids to get points of intersection
#Has to be done by eye for now as math way returns a constant value 
#for some unknown reason?

#Timestamps are including in this code as internal commentry
########################################################

#Plotting the collector current against time 
plt.plot(Epoch,Ic,color='black')

###########################################################
#Set 1 plot all no point of intercept 
###########################################################
#plt.plot_date(x_values,y_1,color='green',label='Set1')
#plt.axhline(y_c1,color='red') #No POIS was going to be achived 

#No Timestamp 

###########################################################
#Set 2 POIs 
###########################################################
#plt.plot_date(x_values,y_2,color='blue',label='Set2')
#plt.axhline(y_c1,color='red') #First centroid

#18:35:00

#####################################################
#plt.plot_date(x_values,y_2,color='blue',label='Set2')
#plt.axhline(y_c2,color='red')#Second Centroid

#18:48:085

#######################################################
#plt.plot_date(x_values,y_2,color='blue',label='Set2')
#plt.axhline(y_c3,color='red')#3rd Centroid


#18:42:49



##########################################################
#SET3 POIS
#########################################################
#plt.plot_date(x_values,y_3,color='yellow',label='Set3')
#plt.axhline(y_c1,color='red') #1st Centroid

#18:47:415

######################################################
#plt.plot_date(x_values,y_3,color='yellow',label='Set3')
#plt.axhline(y_c2,color='red')#2nd Centroid

#18:55:00

######################################################

#plt.plot_date(x_values,y_3,color='yellow',label='Set3')
#plt.axhline(y_c3,color='red')#3rd centroid

#18:52:03




######################################################
#SET4_POIs
######################################################

#plt.plot_date(x_values,y_4,color='red',label='Set4')
#plt.axhline(y_c1,color='pink')#1st dentroid

#17:04:00

####################################################
#plt.plot_date(x_values,y_4,color='red',label='Set4')
#plt.axhline(y_c2,color='pink')#2nd centroid

#17:27:53

####################################################
plt.plot_date(x_values,y_4,color='red',label='Set4')
plt.axhline(y_c3,color='pink')#3rd centroid

#17:13:05




#####################################################
#Fromatting Plots
plt.legend(loc='upper left')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Collector Current (A)')
plt.title('Point of Intersections to detremine start time of RUL model (3RD Centroid)')
plt.grid()
plt.show()