
#在代码中配置matplotlib参数


#设置后续所有的图形使用的线条宽度为2个点, 颜色为红色
import matplotlib.pyplot as plt 
import numpy as np 

t= np.arange(0.0, 1.0, 0.01)

s= np.sin(2* np.pi* t)
# make line red 
plt.rcParams['lines.linewidth']='3'
plt.plot(t,c)

plt.show()



#从CSV文件导入数据
import csv
filename = 'ch02-data.csv'

data= []

try: 
	with open(filename) as f: 
		reader =csv.reader(f)
	header= reader.next()
	data= [row for row in reader]
except csv.Error as e:
	print "Error reading CSV file at line &s: %s" % (reader.line_num, e)
	sys.exit(-1)

if header:
	print header
	print '=================='
for datarow in data:
	print datarow 




#绘制误差条形图 
import numpy as np 
import matplolib.pyplot as plt

# generate number of measurements 
x = np.arange(0, 10, 1)

# values computed from "measured"
y = np.log(x)

# add some error samples from standard normal distribution 
xe = 0.1* np.abs(np.random.randn(len(y)))

# draw and show errorbar 
plt.bar(x,y,yerr=xe, width=0.4, align='center', ecolor='r', color='cyan', label='experiment #1');

# give some explainations 
plt.xlabel ('# measurement')
plt.ylabel ('Measured values')
plt.title('Measurements')
plt.legend(loc='upper left')

plt.show()


#another example (import from txt); note: separate the loading of the data and the plotting 
import numpy as np 
import matplotlib.pyplot as plt 

col0= np.genfromtxt('J.txt', usecols=(0), delimiter=' ', dtype=None)
col1= np.genfromtxt('J.txt', usecols=(1), delimiter=' ', dtype=None)
col2= np.genfromtxt('J.txt', usecols=(2), delimiter=' ', dtype=None)

fig, ax1 = plt.subplots()

ax1.plot(col0, col1, c='b', marker='o', markerdgewidth=0, linewidth=0, markersize=3)
ax1.errorbar(col0, col1, yerr=col2, linestyle=' ', c='b')
plt.show()

# np.genfromtxt [bring the data like what I need]
# ax1.errorbar [put the error bars using yerr value for Y axis]











