import sys
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

parsed=pd.read_csv('/Users/carrielin/Desktop/result/8_result_2.csv',index_col=['condition','run_sequence'])

parsed=parsed.swaplevel('condition','run_sequence').sortlevel(0) #ignore the warning after this line


#save mean of individual data 
parsed=DataFrame(parsed)
#means=parsed['acc'].groupby([parsed['run_sequence'],parsed['condition']]).mean()
means=parsed.groupby(['run_sequence','condition'])[['acc']].mean()

means=means.unstack()

means.to_csv('/Users/carrielin/Desktop/result/8_result_acc_mean.csv')


#get mean of group data
df_all=pd.concat([parsed,parsed2,parsed3],keys=['','',''])
df_all=df_all.swaplevel('condition','run_sequence').sortlevel(0) #ignore the warning after this line


#means=df_all['acc'].groupby([df_all['run_sequence'],df_all['condition']]).mean()
means_all=df_all.groupby(['run_sequence','condition'])[['acc']].mean()

means_all=means_all.unstack()

means_all.to_csv('/Users/carrielin/Desktop/result/all_acc_mean.csv')

#updated on 30 NOV
parsed = parsed.groupby(['','']) #put variable you want to sort by



