import numpy as np, scipy.stats, pandas as pd 

import matplotlib as mpl 
import matplotlib.pyplot as plt 
import pylab as pl 
%matplotlib inline
pd.options.display.mpl_style = 'default'
plt.style.use('ggplot')
mpl.rcParams['font.family'] = ['Bitstream Vera Sans']

data_all=pd.read_csv('/Users/carrielin/Downloads/run-final_del.csv')

#2*2 anova (block_type * judge_type)

blocks = pd.unique(data_all.block_type.values)

d_data = {block:data_all['acc'][data_all.block_type == block] for block in blocks} 

judges = pd.unique(data_all.judge_type.values)

d_data2 = {judge:data_all['acc'][data_all.judge_type == judge] for judge in judges} 

# which graph do you need for this anova? 
width = 0.25
plt.bar(np.arange(1,4)-width,[np.mean(d_data['Control']),np.mean(d_data['Orthogonal'])],width)
plt.bar(np.arange(1,4),[np.mean(d_data2['Segmental']),np.mean(d_data2['Suprasegmental'])],width,color=plt.rcParams['axes.color_cycle'][0])
plt.legend(['block_type','judge_type'],loc=4)
plt.xticks([Control_Seg,Orthogonal_Supra]);


%Rpush d_data['Control'] d_data['Orthogonal'] d_data2['Segmental'] d_data2['Suprasegmental']

%R Factor1 <- c('Control','Orthogonal')
%R Factor2 <- c('Segmental','Suprasegmental')
%R idata <- data.frame(Factor1, Factor2)

#make sure the vectors appear in the same order as they appear in the dataframe
%R Bind <- cbind(d_data['Control'],d_data['Orthogonal'],d_data2['Segmental'],d_data2['Suprasegmental'])
%R model <- lm(Bind~1)

%R library(car)
%R analysis <- Anova(model, idata=idata, idesign=~Factor1*Factor2, type="III")
%R anova_sum = summary(analysis)
%Rpull anova_sum

print anova_sum



