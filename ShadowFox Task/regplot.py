import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

data = {'X_variable': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Y_variable': [2, 4, 5, 4, 6, 7, 9, 8, 10, 11]}
df = pd.DataFrame(data)
sns.regplot(x='X_variable', y='Y_variable', data=df)

plt.show()