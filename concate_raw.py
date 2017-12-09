import sys
from pandas import Series, DataFrame
import pandas as pd 
import numpy as np 


#get run data & make table2 (desc)

data1=pd.read_csv('/Users/carrielin/Downloads/run1-final_1_del.csv')
data1=DataFrame(data1,columns=['RT','condition', 'acc', 'condition1', 'judge_type','RT_Z'])


data2=pd.read_csv('/Users/carrielin/Downloads/run2-final_2_del.csv')
data2=DataFrame(data2,columns=['RT','condition', 'acc', 'condition1', 'judge_type','RT_Z'])

data3=pd.read_csv('/Users/carrielin/Downloads/run3-final_3_del.csv')
data3=DataFrame(data3,columns=['RT','condition', 'acc', 'condition1', 'judge_type','RT_Z'])

data4=pd.read_csv('/Users/carrielin/Downloads/run4-final_4_del.csv')
data4=DataFrame(data4,columns=['RT','condition', 'acc', 'condition1', 'judge_type','RT_Z'])

data5=pd.read_csv('/Users/carrielin/Downloads/run5-final_5_del.csv')
data5=DataFrame(data5,columns=['RT','condition', 'acc', 'condition1', 'judge_type','RT_Z'])

data6=pd.read_csv('/Users/carrielin/Downloads/run6-final_6_del.csv')
data6=DataFrame(data6,columns=['RT','condition', 'acc', 'condition1', 'judge_type','RT_Z'])

data_all=pd.concat([data1,data2,data3,data4,data5,data6])

#data_all=DataFrame(data,columns=['RT','condition', 'acc', 'condition1', 'judge_type','RT_Z'])

data_all.to_csv('/Users/carrielin/Downloads/run-final_del.csv')

data_all.groupby(['judge_type','condition1','condition'])[['acc','RT']].describe()

data_all=pd.read_csv('/Users/carrielin/Downloads/run-final_del.csv')

from scipy import stats 

#Supra = data_all['acc'][data_all.condition1 == 'Suprasegmental']
#Seg = data_all['acc'][data_all.condition1 == 'Segmental']

cd1s = pd.unique(data_all.condition1.values)

d_data = {cd1:data_all['acc'][data_all.condition1 == cd1] for cd1 in cd1s} #'for' 

k = len(pd.unique(data_all.condition1))  # number of conditions
N = len(data_all.values)  # conditions times participants
n = data_all.groupby('condition1').size()[0] #Participants in each condition

F, p = stats.f_oneway(d_data['Vowel'], d_data['Tone'],d_data['Emotion'])

# do one-way repeated measures in rpy2
import numpy as np, scipy.stats, pandas as pd

import matplotlib as mpl 
import matplotlib.pyplot as plt
import pylab as pl 
%matplotlib inline
pd.options.display.mpl_style = 'default'
plt.style.use('ggplot')
mpl.rcParams['font.family'] = ['Bitstream Vera Sans']


data_all=pd.read_csv('/Users/carrielin/Downloads/run-final_del.csv')

cd1s = pd.unique(data_all.condition1.values)

d_data = {cd1:data_all['acc'][data_all.condition1 == cd1] for cd1 in cd1s} 

plt.bar(np.arange(1,4),[np.mean(d_data['Vowel']),np.mean(d_data['Tone']),np.mean(d_data['Emotion'])],align= 'center')
plt.xticks([Vowel, Tone, Emotion])

# do this in jupyter notebook (recommended)

%load_ext rpy2.ipython

#pop the data into R
%Rpush d_data['Vowel'] d_data['Tone'] d_data['Emotion']

#label the conditions
%R Factor <- c('Vowel','Tone','Emotion')
#create a vector of conditions
%R idata <- data.frame(Factor)

#combine data into single matrix
%R Bind <- cbind(d_data['Vowel'],d_data['Tone'],d_data['Emotion'])
#generate linear model
%R model <- lm(Bind~1)

#load the car library. note this library must be installed.
%R library(car)

#run anova
%R analysis <- Anova(model,idata=idata,idesign=~Factor,type="III")
#create anova summary table
%R anova_sum = summary(analysis)

#move the data from R to python
%Rpull anova_sum
print anova_sum




