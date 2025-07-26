import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = sns.load_dataset("tips")
sns.barplot(x='day', y='total_bill', data=data)

plt.show()