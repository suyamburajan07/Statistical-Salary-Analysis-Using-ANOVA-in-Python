import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

google = [120000, 125000, 130000, 115000, 128000]  # Salaries for Google employees
samsung = [95000, 98000, 92000, 97000, 94000]  # Salaries for Samsung employees
apple = [140000, 135000, 142000, 138000, 145000]  # Salaries for Apple employees

data = pd.DataFrame({
    'Company': ['Google'] * len(google) + ['Samsung'] * len(samsung) + ['Apple'] * len(apple),
    'Salary': google + samsung + apple
})

data.to_csv('salary_data.csv', index=False)
print("Raw salary data saved to 'salary_data.csv'.")

f_statistic, p_value = stats.f_oneway(google, samsung, apple)

print(f"F-Statistic: {f_statistic:.2f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant difference in salaries between the companies.")
else:
    print("Fail to reject the null hypothesis: No significant difference in salaries between the companies.")

summary = pd.DataFrame({
    'Company': ['Google', 'Samsung', 'Apple'],
    'Mean Salary': [sum(google) / len(google), sum(samsung) / len(samsung), sum(apple) / len(apple)],
    'StdDev Salary': [pd.Series(google).std(ddof=1), pd.Series(samsung).std(ddof=1), pd.Series(apple).std(ddof=1)]  # ddof=1 for sample std
})

summary.to_csv('salary_summary.csv', index=False)
print("Summary statistics saved to 'salary_summary.csv'.")

plt.figure(figsize=(10, 6))
plt.boxplot([google, samsung, apple], labels=['Google', 'Samsung', 'Apple'])
plt.title('Boxplot of Salaries by Company')
plt.ylabel('Salary')
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(summary['Company'], summary['Mean Salary'], yerr=summary['StdDev Salary'], capsize=5, color=['blue', 'orange', 'green'])
plt.title('Mean Salaries by Company with Standard Deviations')
plt.ylabel('Salary')
plt.show()
