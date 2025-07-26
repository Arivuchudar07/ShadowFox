import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tips = sns.load_dataset("penguins")
sns.scatterplot(x="species",y="flipper_length_mm",hue="sex",data=tips)

plt.show()