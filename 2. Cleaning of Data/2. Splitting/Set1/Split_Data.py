#Last Modified 03/02/2022
#By Saboor Rashid
#This code takes in the cleaned data and splits the data into training and testing data 

import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_pickle("Set_1_Clean")
print (df)

#################################################

#Extracting Variables to be placed into combo groups

Time_Epoch =df.iloc[:,0]
#print(Time_Epoch)

Time_Real = df.iloc[:,1]
#print(Time_Real)

Package_Temp = df.iloc[:,2]
#print(Package_Temp)

Ic = df.iloc[:,3]
#print(Ic)

Vc = df.iloc[:,4]
#print(Vc)

Ig = df.iloc[:,5]
#print(Ig)

Vg = df.iloc[:,6]
#print(Vg)

Rc = df.iloc[:,7]
#print(Rc)

Rg = df.iloc[:,8]
#print(Rg)

Pc = df.iloc[:,9]
#print(Pc)

###############################################################
#Data Frame storing actual values with new variable names 

Data_1=[Time_Epoch,Package_Temp,Ic,Vc,Ig,Vg,Rc,Rg,Pc]
df1nT = pd.DataFrame(Data_1)
df1 = df1nT.T
print(df1) #Floats 

################################################################

#Splitting Data 80/20 split 


Epoch_train, Epoch_test, Temp_train, Temp_test,Ic_train,Ic_test,Vc_train,Vc_test = train_test_split( Time_Epoch, Package_Temp,Ic,Vc,test_size = 0.2, shuffle = False)

Ig_train,Ig_test,Vg_train,Vg_Test,Rc_train,Rc_test,Rg_train,Rg_test,Pc_train,Pc_test = train_test_split(Ig,Vg,Rc,Rg,Pc,test_size=0.2,shuffle=False )

##################################################################
#Assigning Training and Testing Dataframe stored as Pickle format

Data_1P=[Epoch_train,Temp_train,Ic_train,Vc_train,Ig_train,Rc_train,Rg_train,Pc_train]
Train1NT=pd.DataFrame(Data_1P)
Train_1 = Train1NT.T
print(Train_1)

Data_1T = [Epoch_test,Temp_test,Ic_test,Vc_test,Ig_test,Rc_test,Rg_test,Pc_test]
Test1NT = pd.DataFrame(Data_1T)
Test_1 = Test1NT.T
print(Test_1)

Train_1.to_pickle('Set_1_Train_Data.pkl')
Test_1.to_pickle('Set_1_Test_Data.pkl')














