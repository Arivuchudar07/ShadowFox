import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {'Month':['Jan','Feb','Mar','Apr','May','Jun'],
        'Sales':[100, 120, 90, 150, 130, 180]}

df = pd.DataFrame(data)

sns.lineplot(x='Month', y='Sales', data=df)
plt.title("monthly sales trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()