import matplotlib.pyplot as plt
import numpy as np

data = np.array([30,25,20,15,10])

labels = ["Apples","Bananas","Oranges","Grapes","Pineapples"]
plt.pie(data,labels=labels,wedgeprops={"edgecolor":"black","linewidth":1},startangle=90)
plt.title("pie chart")

plt.show()