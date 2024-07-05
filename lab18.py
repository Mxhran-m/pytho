#8.Drawing line chart and Bar chart using Matplotlib
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,8,6,4,2]
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Chart')
plt.show()
x=['a','b','c','d','e']
plt.bar(x,y)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()