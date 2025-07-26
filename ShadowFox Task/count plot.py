import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')
sns.countplot(x='sex',hue='smoker',data=df)

plt.show()
