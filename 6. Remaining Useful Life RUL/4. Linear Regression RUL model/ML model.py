#Last Modified 18/02/2022
#By Saboor Rashid

#Use ML linear regression to predict the RUL of the IGBT


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import matplotlib.pyplot as plt


df = pd.read_pickle('RUL') #Loading data in
#print(df)

###############################################

#Extract variabless

Epoch = df.iloc[:,0]
#print(Epoch)

Countdown= df.iloc[:,1]
#print(Countdown)

##############################################

#Split data 80/20

# Can change on the fly to even 99% testing and 1 %training

Epoch_train, Epoch_test, Countdown_train, Countdown_test = train_test_split(Epoch,Countdown,test_size=0.99,shuffle= False)

###############################################

# Have to reshape Data

X_train = Epoch_train.values.reshape(-1,1)
#print(X_train)

X_test = Epoch_test.values.reshape(-1,1)
#print(X_test)

Y_train = Countdown_train.values.reshape(-1,1)
#print(Y_train)

Y_test = Countdown_test.values.reshape(-1,1)
#print(Y_test)

################################################

# Linear Regression Model

model = linear_model.LinearRegression()

model.fit(X_train,Y_train) # Training the model

Y_pred = model.predict(X_test) # Predicting the model


#######################################################

# Priniting Equation of line and visualising RUL graph


print("Equation of line is y=",model.coef_,"x +",model.intercept_)

plt.plot(X_test,Y_test,color = 'blue')#Orignal Plot
plt.plot_date(X_test,Y_pred,color ='red') #Predicted Plot

plt.xlabel('Time (D:H:M:S)')
plt.ylabel('Remaining useful Life (Epoch)')
plt.title('Remaining useful life of IGBT IRF-G4BC30KD ')

plt.grid()
plt.show()


########################################################

# Exporting Data to an excel file where Epoch RUL can 
# be converted to a time stamp to get RUL in a human format



X_train = X_train.flatten()
#print(X_train)

Y_train = Y_train.flatten()
Y_train = (Y_train/86400)+25569 #Converting the RUL into a EPOCH format for Excel
#print(Y_train)

X_test = X_test.flatten()
#print(X_test)

Y_test = Y_test.flatten()
Y_test = (Y_test/86400)+25569
#print(Y_test)

Y_pred = Y_pred.flatten()
Y_pred = (Y_pred/86400)+25569
#print(Y_pred)

# Saving as a Dataframe and exporting as a XLSX file.

Data_train = [X_train,Y_train,X_test,Y_test,Y_pred]
df2 = pd.DataFrame(Data_train)
df2 = df2.T
df2.columns =['X Train', 'Y Train', 'X Test', 'Y Test','Y Predict']
print(df2)

#df2.to_excel('Output RUL.xlsx')


