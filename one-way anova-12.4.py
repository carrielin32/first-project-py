
import pandas as pd
datafile="PlantGrowth.csv"
data = pd.read_csv(datafile)
 
#Create a boxplot
data.boxplot('weight', by='group', figsize=(12, 8))

#‘group' is the condition name (of your IV)
#‘weight' is the name of your DV
 
ctrl = data['weight'][data.group == 'ctrl']
# 'ctrl' represents 'control'
 
grps = pd.unique(data.group.values)
d_data = {grp:data['weight'][data.group == grp] for grp in grps} #'for' 
 
k = len(pd.unique(data.group))  # number of conditions
N = len(data.values)  # conditions times participants
n = data.groupby('group').size()[0] #Participants in each condition

from scipy import stats 

F, p = stats.f_oneway(d_data['ctrl'], d_data['trtl'],d_data['trt2'])
# 'ctrl' represents control, 'trt1' represents group1, 'trt2' represents group2

# if you use scipy, you need to calculate effect size & df by yoruself, however. 

DFbetween = k - 1
DFwithin = N - k 
DFtotal = N - 1 

# input formula of effect size below: 








