import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,8,6,2,4])
y = np.array([9,3,6,5,1])

plt.fill_between(x,y)
plt.title("area chart")

plt.show()