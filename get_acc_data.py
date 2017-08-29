#this script: used to calculate acc of each trial 

import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#for this example, 'run2' is a vowel task, if item=/ba/, then correct_key=/+Shift/, else correct response is /+Right Shift/
parsed=pd.read_csv('/Users/carrielin/Desktop/run2-acc.csv')

parsed['resp_item']=parsed['respKey'].replace('+Shift .','ba')
parsed['resp_item']=parsed['resp_item'].replace('+Right Shift .','bu')


parsed['acc']=np.where((parsed['resp_item']==parsed['item_2']),'1','0')

parsed.to_csv('/Users/carrielin/Desktop/run2-acc.csv')



