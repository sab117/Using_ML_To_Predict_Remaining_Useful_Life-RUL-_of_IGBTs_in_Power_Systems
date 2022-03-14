#Last Modifed 07/03/2022
#By Saboor Rashid
#Creates an ML model use Linear Regression 
#Collector Current Only 


import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_pickle("Set_1_Train_Data.pkl")
df1 = pd.read_pickle("Set_1_Test_Data.pkl")
print(df)
#print(df1)

################################################################

#Loading in the Time data 

Time_Epoch_Train = df.iloc[:,0]
#print(Time_Epoch_Train)
X_Train = Time_Epoch_Train.values.reshape(-1,1) #Makes a 1D array 
print(X_Train)

Time_Epoch_Test = df1.iloc[:,0]
#print(Time_Epoch_Test)
X_Test = Time_Epoch_Test.values.reshape(-1,1)
print(X_Test)


####################################################

#Loading in the collector voltage Data 

Ic_Train = df.iloc[:,2]
#print(Vc_Train)
Y_Train = Ic_Train.values.reshape(-1,1)
#print(Y_Train)

Ic_Test = df1.iloc[:,2]
#print(Vc_Test)
Y_Test = Ic_Test.values.reshape(-1,1)
#print(Y_Test)

####################################################



model_1= linear_model.LinearRegression() #Linear Regression for collector voltage 

model_1.fit(X_Train,Y_Train)

Y_pred_1 = model_1.predict(X_Test)

print("Coefficients: \n", model_1.coef_)
print("Intercept: \n",model_1.intercept_)

print("Equation of line is y=",model_1.coef_, "x +", model_1.intercept_)




# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(Y_Test, Y_pred_1))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(Y_Test, Y_pred_1))

plt.plot(X_Test,Y_Test,color='red')
plt.plot_date(X_Test,Y_pred_1,color='blue')
plt.grid()
plt.xlabel('Time D:H:M:S')
plt.ylabel('Collector Current (A)')
plt.title('Average collector current Linear Regression model (1st Hour of Data)')
plt.show()
