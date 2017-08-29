import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#delete 'no response' cleanly before enter raw data


#read your csv/txt first, combine two rows into one 
data=pd.read_table('/Users/carrielin/Desktop/run1.txt',header=None)
data=DataFrame(data.values.reshape(-1,2))
#data.to_csv('/Users/carrielin/Desktop/run1.csv')
#data=DataFrame(data.reshape(-1,2)) 


#split one column into several columns 
data_col=DataFrame(data.ix[:,1]) #select column[1] 
data_col.to_csv('/Users/carrielin/Desktop/run1-2-2.csv')

data_col=pd.read_csv('/Users/carrielin/Desktop/run1-2-2.csv') #in this step, hearder back to Default 

data_col=data_col['1'].str.split(',',expand=True) #get 'rt' and 'respKey'
data_col.to_csv('/Users/carrielin/Desktop/run1-2-2.csv')
#delete last two columns first

#delete 'drop' column
data_col=pd.read_csv('/Users/carrielin/Desktop/run1-2-2.csv',names=['RT','respKey','drop'])
data_col=DataFrame(data_col,columns=['RT','respKey','drop'])

data_col=data_col.drop('drop',axis=1) #get 'rt' and 'respKey'

#merge data_item and data_col to one 
data_item=DataFrame(data.ix[:,0]) #select column[0]
data_merge=pd.merge(data_item,data_col,how='outer',left_index=True,right_index=True)

#cut numbers in 'respKey' column 
data_merge['respKey'] = data_merge['respKey'].str.replace('\d+', '')  #'\d' refer to any digit, '+' for 'one or more'


data_merge.to_csv('/Users/carrielin/Desktop/run1-result.csv')

#add subject number manually 