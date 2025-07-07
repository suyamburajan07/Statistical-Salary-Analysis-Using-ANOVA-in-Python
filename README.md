# Statistical Salary Analysis Using ANOVA in Python

This project demonstrates how to perform **Analysis of Variance (ANOVA)** using Python to compare employee salaries across different companies. The project supports both **synthetic (random)** and **user-input** datasets and provides insights using statistical tests and visualizations.

---

## Overview

The goal of this project is to determine whether there are statistically significant differences in mean salaries between companies (e.g., Google, Samsung, Apple) using ANOVA. The code is designed for flexibility and supports:

- **Option 1**: Automatically generated random salary data
- **Option 2**: Manually entered salary values by the user

---

## Features

- Generate or input salary data for three companies
- Perform one-way ANOVA test (`scipy.stats.f_oneway`)
- Compute and export summary statistics (mean, standard deviation)
- Visualize data using:
  - Boxplots for salary distributions
  - Bar charts for mean salaries with error bars
- Export data and results to CSV files

---

## Technologies Used

- Python 3.x
- Pandas
- SciPy
- NumPy
- Matplotlib

---

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/suyamburajan07/Statistical-Salary-Analysis-Using-ANOVA-in-Python.git
   cd Statistical-Salary-Analysis-Using-ANOVA-in-Python
