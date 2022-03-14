#Last modified 05/03/2022
#By Saboor Rashid
#Visualisation of Full Data with Scatter and Line Plots

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_pickle("Full_Set_Clean")
#print(type(df))
print(df)

################################################################################

#Scatter Plots of The full Data set

df.plot(x = 'Time', y='Package Temp', kind= 'scatter',color = 'red')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Temperature Degrees Celcius')
plt.title('Teperature of IGBT Package over Time ')
plt.grid()


df.plot(x = 'Time', y='Collector Current', kind= 'scatter')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Current (A)')
plt.title('Collector Current of IGBT Package over Time ')
plt.grid()

df.plot(x = 'Time', y='Collector Voltage', kind= 'scatter')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Cllector Voltage (V)')
plt.title('Collector Voltage of IGBT Package over Time ')
plt.grid()

df.plot(x = 'Time', y='Gate Current', kind= 'scatter',color = 'green')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Current (A)')
plt.title('Gate Current of IGBT Package over Time ')
plt.grid()

df.plot(x = 'Time', y='Gate Voltage', kind= 'scatter',color = 'green')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Voltage (V)')
plt.title('Gate Voltage of IGBT Package over Time ')
plt.grid()

df.plot(x = 'Time', y='Collector Resistance', kind= 'scatter')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Resistace (Ohms)')
plt.title('Colletor Resistance Vs Time ')
plt.grid()

df.plot(x = 'Time', y='Gate Resistance ', kind= 'scatter') #There is an accidental Space with this name for Y value 
plt.xlabel('Time D:H:M:S')
plt.ylabel('Resistace (Ohms)')
plt.title('Gate Resistance Vs Time ')
plt.grid()

df.plot(x = 'Time', y='Collector Power', kind= 'scatter') #There is an accidental Space with this name for Y value 
plt.xlabel('Time D:H:M:S')
plt.ylabel('Power (W)')
plt.title('Collector Power Vs Time ')
plt.grid()


#############################################################################

#Line Plots of the full data set

df.plot(x = 'Time', y='Package Temp', kind= 'line',color = 'red')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Temperature Degrees Celcius')
plt.title('Temperature of IGBT Package over Time ')
plt.grid()


df.plot(x = 'Time', y='Collector Current', kind= 'line')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Current (A)')
plt.title('Collector Current of IGBT Package over Time ')
plt.grid()


df.plot(x = 'Time', y='Collector Voltage', kind= 'line')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Current (V)')
plt.title('Collector Voltage of IGBT Package over Time ')
plt.grid()


df.plot(x = 'Time', y='Gate Current', kind= 'line',color = 'green')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Current (A)')
plt.title('Gate Current of IGBT Package over Time ')
plt.grid()


df.plot(x = 'Time', y='Gate Voltage', kind= 'line',color = 'green')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Voltage (A)')
plt.title('Gate Voltage of IGBT Package over Time ')
plt.grid()

df.plot(x = 'Time', y='Collector Resistance', kind= 'line')
plt.xlabel('Time D:H:M:S')
plt.ylabel('Resistace (Ohms)')
plt.title('Colletor Resistance Vs Time ')
plt.grid()

df.plot(x = 'Time', y='Gate Resistance ', kind= 'line') #Space here as well
plt.xlabel('Time D:H:M:S')
plt.ylabel('Resistace (Ohms)')
plt.title('Gate Resistance Vs Time ')
plt.grid()

df.plot(x = 'Time', y='Collector Power', kind= 'line') #There is an accidental Space with this name for Y value 
plt.xlabel('Time D:H:M:S')
plt.ylabel('Power (W)')
plt.title('Collector Power Vs Time ')
plt.grid()

plt.show()