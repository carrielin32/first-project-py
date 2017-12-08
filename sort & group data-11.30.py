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


#updated on 30 NOV
#get task type first (3 level: vowel, tone, emotion)
parsed=pd.read_csv('')

#used for run1 & run2
parsed['condition1'] = np.where(parsed['condition'].isin(['V/T','V/E','V/B']),'Vowel',parsed['condition1'])

#get block type (2 level: control, orthogonal)
parsed['block'] = np.where((parsed['condition']=='V/B'),'Control','Orthogonal')

#get judgment type (2 level: segmental, suprasegmental)
# parsed['judge_type']= np.where((parsed['condition1']=='Vowel'),'Segmental','Suprasegmental')
# if you concate manually, you do not need the step above. 

parsed.to_csv('')

#_______
#used for run3 & run4

parsed=pd.read_csv('')

parsed['condition1'] = np.where(parsed['condition'].isin(['T/V','T/E','T/B']),'Tone',parsed['condition1'])
parsed['block'] = np.where((parsed['condition']=='T/B'),'Control','Orthogonal')


parsed.to_csv('')

#_______
#used for run5 & run6
parsed['condition1'] = np.where(parsed['condition'].isin(['E/V','E/T','E/B']),'Emotion',parsed['condition1'])
parsed['block'] = np.where((parsed['condition']=='E/B'),'Control','Orthogonal')

parsed.to_csv('')


#concate all CSV. 
#now get your judge_type (2 level: Segmental, Suprasegmental )


#_______
#get size of interference [ equals RT(Orthogonal)-RT(Control) ]
# condition1 (3 level: Vowel, Tone, Emotion)

# interference (V/T-V/B, V/E-V/B, T/V-T/B, T/E-T/B, E/T-E/B, E/V-E/B)
# should calculated separately in each run of data 
parsed=parsed.groupby(['judge_type','condition1'])[['interference']]


# delete RT greater than 3SD


import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from scipy import stats

data=pd.read_csv('/Users/carrielin/Downloads/run1-final_1.csv')

data=DataFrame(data,columns=['RT','condition', 'acc', 'condition1', 'judge_type'])

# data=data.groupby(['judge_type','condition','condition1'])[['RT','acc']]

a=np.array(data['RT'])

data['RT_Z']=stats.zscore(a)

b=np.array(data['RT_Z'])

#(np.abs((b)>3)).any(1)

b[np.abs(b) > 3]

data.to_csv('/Users/carrielin/Downloads/run1-final_1.csv')

# add and delete outliers manually 











