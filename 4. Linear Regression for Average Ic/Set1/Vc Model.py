#Last Modifed 03/02/2022
#By Saboor Rashid
#Creates an ML model use Linear Regression 
#Collector Voltage Only 

from pickle import TRUE
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_pickle("Set_1_Train_Data.pkl")
df1 = pd.read_pickle("Set_1_Test_Data.pkl")
#print(df)
#print(df1)

################################################################

#Loading in the Time data 

Time_Epoch_Train = df.iloc[:,0]
#print(Time_Epoch_Train)
X_Train_1 = Time_Epoch_Train.values.reshape(-1,1) #Makes a 1D array 
#print(X_Train)

Time_Epoch_Test = df1.iloc[:,0]
#print(Time_Epoch_Test)
X_Test_1 = Time_Epoch_Test.values.reshape(-1,1)
#print(X_Test)


####################################################

#Loading in the collector voltage Data 

Vc_Train = df.iloc[:,3]
#print(Vc_Train)
Y_Train_1 = Vc_Train.values.reshape(-1,1)
#print(Y_Train)

Vc_Test = df1.iloc[:,3]
#print(Vc_Test)
Y_Test_1 = Vc_Test.values.reshape(-1,1)
#print(Y_Test)

####################################################



model_1= linear_model.LinearRegression(fit_intercept=True,normalize=True,n_jobs=1) #Linear Regression for collector voltage 

model_1.fit(X_Train_1,Y_Train_1)

Y_pred_1 = model_1.predict(X_Test_1)

print("Coefficients: \n", model_1.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(Y_Test_1, Y_pred_1))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(Y_Test_1, Y_pred_1))

plt.plot(X_Test_1,Y_Test_1,color='red')
plt.plot(X_Test_1,Y_pred_1,color='blue')
plt.show()
