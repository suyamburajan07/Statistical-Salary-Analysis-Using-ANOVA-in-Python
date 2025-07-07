import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42)
group1 = np.random.normal(loc=50, scale=5, size=30)
group2 = np.random.normal(loc=55, scale=5, size=30)
group3 = np.random.normal(loc=60, scale=5, size=30)


data = pd.DataFrame({
    'Group': ['Group1'] * len(group1) + ['Group2'] * len(group2) + ['Group3'] * len(group3),
    'Scores': np.concatenate([group1, group2, group3])
})

print(data.head())
print(data.describe())

f_statistic, p_value = stats.f_oneway(group1, group2, group3)

print(f"F-Statistic: {f_statistic:.2f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant difference between the group means.")
else:
    print("Fail to reject the null hypothesis: No significant difference between the group means.")

plt.figure(figsize=(10, 6))
plt.boxplot([group1, group2, group3], labels=['Group1', 'Group2', 'Group3'])
plt.title('Boxplot of Group Scores')
plt.ylabel('Scores')
plt.show()

group_means = [np.mean(group) for group in [group1, group2, group3]]
group_std = [np.std(group) for group in [group1, group2, group3]]

plt.figure(figsize=(10, 6))
plt.bar(['Group1', 'Group2', 'Group3'], group_means, yerr=group_std, capsize=5, color=['blue', 'orange', 'green'])
plt.title('Group Means with Standard Deviation')
plt.ylabel('Mean Score')
plt.show()

data.to_csv('anova_data.csv', index=False)
results = pd.DataFrame({
    'Group': ['Group1', 'Group2', 'Group3'],
    'Mean': group_means,
    'StdDev': group_std
})
results.to_csv('anova_results.csv', index=False)