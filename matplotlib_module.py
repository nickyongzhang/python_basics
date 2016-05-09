from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

# You can comment the line below to use the default matplotlib style
style.use('ggplot')

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

# can plot specifically, after just showing the defaults:
# plot line 
plt.plot(x,y,'g',label='line one', linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)


plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()
 
plt.grid(True,color='k')

plt.show()

# plot bar
plt.bar(x, y, align='center')
 
plt.bar(x2, y2, color='g', align='center')
 
 
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
 
plt.show()

# plot scatter
plt.scatter(x, y)#, align='center')
 
plt.scatter(x2, y2, color='g')#, align='center')
 
 
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
 
plt.show()

# plot from a csv or txt file 
# try change the file into exampleCsv.txt
x,y = np.loadtxt('examplefile.csv',
                 unpack=True,
                 delimiter = ',')
 
plt.plot(x,y)
 
plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
 
plt.show()