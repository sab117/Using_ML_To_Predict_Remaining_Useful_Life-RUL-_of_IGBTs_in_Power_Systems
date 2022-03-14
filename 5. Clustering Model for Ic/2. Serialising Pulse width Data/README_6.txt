Last Modified 23/02/2022
By Saboor Rashid

"Training Serialisation Folder" --> Taking the pulse width data to be used for cluster model and serialised data into the pickle format for Training Data
"Testing Serialisation Folder"--> Taking the pulse width data to be used for cluster model and serialised data into the pickle format for Testing Data

"Cluster Data Serialisation Folder" --> This folder combines the full training and testing data together to create the full data set to be used in the cluster model. This
was achived by concatanating the two pickle files from the trainig and Testing folder. Actual code to do this went missing after a while :(

It was redone and achieved by just using excel and copying the training data into a seprerate excle file and the testing data was appended to the bottom of the training data
to create the full data to be used for the model

