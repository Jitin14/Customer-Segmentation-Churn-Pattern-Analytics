# Customer Segmentation & Churn Pattern Analytics in European Banking

## Overview
This project analyzes customer churn patterns in a European bank dataset. Using segmentation techniques and visual analytics, it uncovers demographic, financial, and behavioral drivers of customer attrition. The goal is to provide actionable insights for banking decision-makers to design targeted, data-driven retention strategies.

## Project Author

By: Jitin Raju
Guided by: Mr. Saiprasad Kagne

## Features
- Data cleaning and preparation (handling missing values, duplicates, categorical conversions).

## Customer segmentation based on:

- Age Groups
- Credit Score Bands
- Tenure Groups
- Balance Segments
- Churn distribution analysis with visualizations (pie charts, bar plots).
- Comparative profiling of churned vs. retained customers.
- Insights into demographic and financial risk factors.

## Key Takeaways
- Mid-tenure, middle-aged customers with low balances and low credit scores are the most vulnerable to churn.
- Inactive customers churn far more than active ones → engagement programs are critical.
- Zero-balance customers are the largest churn group, but high-balance churners pose the biggest revenue risk.
- Geography and gender differences matter → churn prevention strategies should be tailored by demographic.
- Financial stability indicators (credit score, salary, balance) strongly correlate with churn.

## Tools & Libraries
- Python
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- streamlit

## Dataset
European Bank Customer Dataset (Unified Mentors Project)

## How to Run
**Clone this repository:**

git clone https://github.com/Jitin14/Customer-Segmentation-Churn-Pattern-Analytics.git

**Navigate to the project folder:**

- cd 01_European_bank

**Install dependencies:**

- pip install -r requirements.txt

**Launch Jupyter Notebook:**

- jupyter notebook

**Open the notebook located at:**

- 01_European_bank/Notebook/European Bank.ipynb

**Run the cells sequentially to reproduce the analysis.**

**Or, if you want to explore the interactive dashboard:**

- streamlit run app.py

## References
- Gupta, S., & Lehmann, D. R. (2003). Customers as assets. Journal of Interactive Marketing, 17(1), 9–24.

- Verbeke, W., Martens, D., & Baesens, B. (2011). Social network analysis for customer churn prediction. Applied Soft Computing, 11(3), 221–230.

- European Banking Authority (2024). Customer retention and risk management in EU banks. Annual Report.