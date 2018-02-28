
import numpy as np 
import matplotlib.pyplot as plt 

d1label = ['V/E','E/V']
data1 =[20, 35]
error1=[2, 3]
d2label = ['V/B','E/B']
data2 =[25, 32] 
error2=[3, 5]

width = 0.42

data= np.concatenate([data1, data2])
labels = np.concatenate([d1label, d2label])
yerrs=np.concatenate([error1, error2])
colors = np.repeat(["b","m"], [len(data1), len(data2)])
idx = np.arange(len(data1))
x = np.concatenate([idx, idx+width])
rects=plt.bar(x, data, width=0.42, color=colors, yerr=yerrs)
ax = plt.gca()
ax.set_xticks(x) #put xtick in the middle of the bar, finally...
ax.set_xticklabels(labels)

ax.set_ylabel('Reaction Time(log-transformed)')
ax.legend((rects[0],rects[2]),('Orthogonal','Control')) #rects[2] represents 2nd kind of bar, finally... 


plt.show()

