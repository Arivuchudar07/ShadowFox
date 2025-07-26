import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(200,50,100)
fig = plt.figure(figsize=(3,3))
plt.hist(x,bins=10,color="white",edgecolor="blue")

plt.show()