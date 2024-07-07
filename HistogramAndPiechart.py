#9. Drawjng Histogram and Pte chart using Matplotlib error
import matplotlib.pyplot as plt
data [1,1,2,2,2,3,3,4,5,5,5,5]
plt.hist(data,bins=5)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
labels = ['Apples', 'Bananas', 'Oranges', 'Grapes']
sizes = (30, 25, 20.151)
plt.pie(sizes. labels-labels,autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()