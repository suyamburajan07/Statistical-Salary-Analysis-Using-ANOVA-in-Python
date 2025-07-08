# Import necessary libraries
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Step 1: Manually Input Scores for Each Group
group1 = [52.48, 49.23, 50.13, 47.56, 53.26]
group2 = [56.15, 55.87, 54.91, 53.76, 57.89]
group3 = [59.02, 60.71, 57.89, 61.34, 58.45]

# Step 2: Combine Data into a DataFrame
data = pd.DataFrame({
    'Group': ['Group1'] * len(group1) + ['Group2'] * len(group2) + ['Group3'] * len(group3),
    'Scores': group1 + group2 + group3
})

# Save the raw data to a CSV file
data.to_csv('manual_input_data.csv', index=False)
print("Raw data saved to 'manual_input_data.csv'.")

# Step 3: Perform ANOVA Test
f_statistic, p_value = stats.f_oneway(group1, group2, group3)

# Display the ANOVA results
print(f"F-Statistic: {f_statistic:.2f}")
print(f"P-Value: {p_value:.4f}")

# Interpret the results
if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant difference between the group means.")
else:
    print("Fail to reject the null hypothesis: No significant difference between the group means.")

# Step 4: Calculate Summary Statistics
summary = pd.DataFrame({
    'Group': ['Group1', 'Group2', 'Group3'],
    'Mean': [sum(group1) / len(group1), sum(group2) / len(group2), sum(group3) / len(group3)],
    'StdDev': [pd.Series(group1).std(ddof=1), pd.Series(group2).std(ddof=1), pd.Series(group3).std(ddof=1)]  # ddof=1 for sample std
})

# Save summary statistics to a CSV file
summary.to_csv('manual_input_results.csv', index=False)
print("Summary statistics saved to 'manual_input_results.csv'.")

# Step 5: Visualize the Results
# Boxplot of group scores
plt.figure(figsize=(10, 6))
plt.boxplot([group1, group2, group3], labels=['Group1', 'Group2', 'Group3'])
plt.title('Boxplot of Group Scores')
plt.ylabel('Scores')
plt.show()

# Bar plot of group means with standard deviations
plt.figure(figsize=(10, 6))
plt.bar(summary['Group'], summary['Mean'], yerr=summary['StdDev'], capsize=5, color=['blue', 'orange', 'green'])
plt.title('Group Means with Standard Deviations')
plt.ylabel('Mean Scores')
plt.show()
