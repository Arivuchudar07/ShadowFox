import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

data = {'Category':['A','A','A','B','B','B','C','C','C'],
        'Value':[10,12,15,20,22,25,30,32,35]}
df = pd.DataFrame(data)
sns.boxplot(x='Category',y='Value',data=df)

plt.show()