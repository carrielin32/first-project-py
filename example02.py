
#Barchart (barchart_demo1.png)

#a bar plot with errorbars and height labels on individual bars 

import numpy as np 
import matplotlib.pyplot as plt 

N = 5
men_means = (20, 35, 30, 35, 27)
men_std = (2, 3, 4, 1, 2)

ind = np.arange(N) # the x locations for the groups 
width = 0.35 

fig, ax = plt.subplots()
rects1= ax.bar(ind, men_means, width, color='r', yerr=men_std)

women_means = (25, 32, 34, 20, 25)
women_std = (3, 5, 2, 3, 3)
rects2 = ax.bar(ind + width, women_means, width, color='y', yerr=women_std)

# add some text for labels, title and axes ticks 
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklables(('G1', 'G2', 'G3', 'G4','G5'))

ax.legend((rects1[0],rects2[0]),('Men','Women'))


def autolabel(rects):

# attach a text label above each bar displaying its height 

   for rect in rects:
   	   height = rect.get_height()
   	   ax.text(rect.get_x() + rect.get_width()/2., 1.05*height, 
   	   	       '%d' % int(height), 
   	   	       ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

plt.show()


#### for figure1 


import numpy as np 
import matplotlib.pyplot as plt 

N = 2
orthogonal_means = (20, 35)
orthogonal_std = (2, 3)

ind = np.arange(N) # the x locations for the groups 
width = 0.45 

fig, ax = plt.subplots()
rects1= ax.bar(ind, orthogonal_means, width, color='b', yerr=orthogonal_std)

control_means = (25, 32)
control_std = (3, 5)
rects2 = ax.bar(ind + width, control_means, width, color='m', yerr=control_std)

# add some text for labels, title and axes ticks 
ax.set_ylabel('Reaction Time(log-transformed)')
ax.set_xticks(ind / 2)
ax.set_xticklables(('V/E', 'V/B', 'E/V', 'E/B'))

ax.legend((rects1[0],rects2[0]),('Orthogonal','Control'))

plt.show()

### example 03 [separate labels within each group]

import numpy as np 
import matplotlib.pyplot as plt 

#d1label = ['data1a','data2a']
#data1 = [204.24, 224.24]
#d2label = ['data1b', 'data2b']
#data2 = [206.24, 226.24]
#d3label = ['data1c','data2c']
#data3 = [208.24, 228.24]

d1label = ['V/E','E/V']
data1 =[20, 35]
error1=[2, 3]
d2label = ['V/B','E/B']
data2 =[25, 32] 
error2=[3, 5]

width = 0.42

#data= np.concatenate([data1, data2, data3])
#labels = np.concatenate([d1label, d2label, d3label])
#colors = np.repeat(["r","g","b"], [len(data1), len(data2), len(data3)])
#idx = np.arange(len(data1))
#x = np.concatenate ([idx, idx+width, idx+width*2])
#plt.bar(x, data, width=0.3, color=colors)
#ax = plt.gca()
#ax.set_xticks(x+ width*0.5)
#ax.set_xticklables(labels)

data= np.concatenate([data1, data2])
labels = np.concatenate([d1label, d2label])
yerrs=np.concatenate([error1, error2])
colors = np.repeat(["b","m"], [len(data1), len(data2)])
idx = np.arange(len(data1))
x = np.concatenate([idx, idx+width])
plt.bar(x, data, width=0.42, color=colors, yerr=yerrs)
ax = plt.gca()
ax.set_xticks(x) #put xtick in the middle of the bar, finally...
ax.set_xticklabels(labels)

ax.set_ylabel('Reaction Time(log-transformed)')
#ax.legend((data1[0],data2[0]),('Orthogonal','Control'))


plt.show()






