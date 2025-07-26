import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
sns.histplot(data=tips, x="total_bill")
plt.title("Distribution of Total Bill Amounts")
plt.xlabel("Total bill")
plt.ylabel("Frequency")

plt.show()