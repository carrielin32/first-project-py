import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt 

df8=pd.read_csv('/Users/carrielin/Desktop/result/8_result_2.csv')

df8['stimuli']=df8['stimuli'].str[:3]

df8['stimuli']=df8['stimuli'].replace('ba2','ba,tone2')
df8['stimuli']=df8['stimuli'].replace('ba4','ba,tone4')
df8['stimuli']=df8['stimuli'].replace('da2','da,tone2')
df8['stimuli']=df8['stimuli'].replace('da4','da,tone4')

df8_acc=df8['stimuli']
df8_acc=df8_acc.get_values()
df8_acc[0].str.split(',',1,expand=True).to_csv('/Users/carrielin/Desktop/result/8_result_acc.csv')


df8_acc=pd.read_csv('/Users/carrielin/Desktop/result/8_result_acc.csv')
df8_acc['acc']=np.where((df8_acc['respKey']==df8_acc['consonant']) | (df8_acc['respKey']==df8_acc['tone']),'1','0')
df8_acc['acc'].to_csv('/Users/carrielin/Desktop/result/acc_result.csv')