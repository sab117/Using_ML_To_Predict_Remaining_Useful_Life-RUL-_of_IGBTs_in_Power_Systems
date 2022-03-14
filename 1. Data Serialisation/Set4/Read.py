#Last modified 03/02/2022
#By Saboor Rashid
#Code converts Excel code to a pickle file
#Code is actually from this website "https://www.geeksforgeeks.org/how-to-read-all-excel-files-under-a-directory-as-a-pandas-dataframe/"




import pandas as pd
import os
import glob

  
  
# use glob to get all the xlsx files
# in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.xlsx"))
  
  
# loop over the list of csv files
for f in csv_files:
    
    # read the csv file
    df = pd.read_excel(f)
      
    # print the location and filename
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])
      
    # print the content
    print('Content:')
    #display(df)
    print(df)
    df.to_pickle("Set_4")
