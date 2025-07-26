import matplotlib.pyplot as plt
import numpy as np

years = np.array([2000,2001,2002,2003,2004])
sales = np.array([25000,40000,15000,18000,20000])

plt.bar(years,sales)

plt.xlabel("years")
plt.ylabel("sales")
plt.title("bar graph")

plt.show()