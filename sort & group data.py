#this script: used to sort raw data output 'run1-result.csv' & group data for further mean/acc calculation

import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

parsed=pd.read_csv('/Users/carrielin/Desktop/run2-result.csv')
parsed['item']=parsed['item'].str[-3:]
parsed.to_csv('/Users/carrielin/Desktop/run2-result.csv')


#get item numbers only, last 3 str
#parsed=DataFrame(parsed,index=['item'])
#parsed.to_csv('/Users/carrielin/Desktop/run2-mean.csv')

#! need further check after this step 

parsed=pd.read_csv('/Users/carrielin/Desktop/run2-result.csv')


parsed['item_2'] = np.where(parsed['item'].isin(['121','123','239','127','129','132','134','137','139','221']),'ba', parsed['item_2'])
parsed['item_2'] = np.where(parsed['item'].isin(['122','124','240','128','130','133','135','138','140','222']),'bu', parsed['item_2'])
#parsed['item'] = np.where(parsed['item'].isin(['101','103','201','107','109','112','114','117','119','204']),'tone2', parsed['item'])
#parsed['item'] = np.where(parsed['item'].isin(['102','104','202','108','110','113','115','118','120','205']),'tone4', parsed['item'])


#remember to save these results 
parsed.to_csv('/Users/carrielin/Desktop/run2-acc.csv')
#add item_ori column from 'run2-result-2.csv' to new csv 


#get condition column 
parsed=pd.read_csv('/Users/carrielin/Desktop/run2-acc.csv')

parsed['condition'] = np.where(parsed['item'].isin(['121','122','123','124','132','133','134','135']),'V/T', parsed['condition'])
parsed['condition'] = np.where(parsed['item'].isin(['239','240','221','222']),'V/B', parsed['condition'])
parsed['condition'] = np.where(parsed['item'].isin(['127','128','129','130','137','138','139','140']),'V/E', parsed['condition'])

parsed.to_csv('/Users/carrielin/Desktop/run2-acc.csv')











