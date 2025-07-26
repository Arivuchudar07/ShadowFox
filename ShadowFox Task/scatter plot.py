import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(15)
y = np.random.rand(15)

plt.scatter(x,y,c="b")
plt.title("scatter plot")

plt.show()