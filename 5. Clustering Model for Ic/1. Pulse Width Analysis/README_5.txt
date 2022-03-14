Last Modified 23/02/2022
By Saboor Rashid

"Full Set" --> Contains code on getting the pulse width of the Ic values i.e. getting the data for the cluster model. The code gets the following values for the cluster model
- The X values of Time difference in Epoch
- The Y values of the Ic value in Amps
- Other Data includes the original time stamps M1 and M2, diffence between M1 and M2 yeilds the X values

Data used in all the folder comes from the cleaning folder--> splitting folder



Two excel files are created, one containing the training data values the other the testing data values. Data contains the noise of the Ic values as well

The 'Filter Data' folder contains the actual data to be used for the clustering model. This folder contains 2 excel files it has eliminate the noise in the data 
and return the true pulse width values need for the model.


"Sets 1-4" --> Exactly the same as "Full Set" except data is done by 1 hour sections. This is simply to confirm that the data found in that particualar section is also 
exhbited in the Full set data. 

"Graphs" --> Contains some graphs that were used in the final report