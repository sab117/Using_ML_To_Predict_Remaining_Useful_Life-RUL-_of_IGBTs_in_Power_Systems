Last Modified 23/02/2022
By Saboor Rashid

"Start Time for RUL folder" --> This folder contains the code on getting the start time of the RUL model. It also contains a "graph folder" showing the outputs from the code.
					  Each graph was given a straight red line this corrosponded to the centrid values found in the cluster model. Set 2 and Set 3 point of intersection determines the value for the start of thr
					  RUL model.

"Count Down Values folder" --> This folder contains the excel data. The start time determined in the previous folder was plugged into the excel time data to create the countdown values
					 for the RUL.
					 "Full Set Folder"--> Contains the Raw Data
					 "RUL_Values Folder" --> Contains the time diffrence from before and after the start time of the RUL model
					 "RUL_Values_Filtered" --> Contians the RUL from the start time of the RUL to the end of the data.This is the data used for the RUL model.
					 
"RUL serialisation folder " -->Serialising the RUL_Valies_Filtered data into pickle

"Linear Regression RUL model folder" --> Contains RUL model by using Linear regression. It does show over fitting, but this is explained in the report accompanying this project