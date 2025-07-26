import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,3,5,7,9])
y1 = np.array([2,3,4,5,6])
y2 = np.array([3,4,5,6,7])

plt.stackplot(x,y1,y2)
plt.title("area chart")

plt.show()