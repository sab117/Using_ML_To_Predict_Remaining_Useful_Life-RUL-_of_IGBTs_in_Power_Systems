#Last Modifed 03/02/2022
#By Saboor Rashid
# Model of Collector voltage 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_pickle("Set_2_Train_Data.pkl")
df1 = pd.read_pickle("Set_2_Test_Data.pkl")
#print(df)
#print(df1)


Time_Epoch_Train = df.iloc[:,0]
#print(Time_Epoch_Train)
X_Train = Time_Epoch_Train.values.reshape(-1,1)
#print(X_Train)

Time_Epoch_Test = df1.iloc[:,0]
#print(Time_Epoch_Test)
X_Test = Time_Epoch_Test.values.reshape(-1,1)
#print(X_Test)


Vc_Train = df.iloc[:,3]
#print(Vc_Train)
Y_Train = Vc_Train.values.reshape(-1,1)
#print(Y_Train)

Vc_Test = df1.iloc[:,3]
#print(Vc_Test)
Y_Test = Vc_Test.values.reshape(-1,1)
#print(Y_Test)

###########################################

model = linear_model.LinearRegression()

model.fit(X_Train,Y_Train)

Y_pred = model.predict(X_Test)


print("Coefficients: \n", model.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(Y_Test, Y_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(Y_Test, Y_pred))

plt.scatter(X_Test,Y_Test,color='red')
plt.plot(X_Test,Y_pred,color='blue')
plt.show()