# Customer Segmentation & Churn Pattern Analytics in European Banking

## Overview
This project analyzes customer churn patterns in a European bank dataset. Using segmentation techniques and visual analytics, it uncovers demographic, financial, and behavioral drivers of customer attrition. The goal is to provide actionable insights for banking decision-makers to design targeted, data-driven retention strategies.

## Project Author
- **By:** Jitin Raju  
- **Guided by:** Mr. Sai Prasad Kagne  

## Features
- Data cleaning and preparation (handling missing values, duplicates, categorical conversions).
- Customer segmentation based on:
  - Age Groups
  - Credit Score Bands
  - Tenure Groups
  - Balance Segments
- Churn distribution analysis with visualizations (pie charts, bar plots).
- Comparative profiling of churned vs. retained customers.
- Insights into demographic and financial risk factors.

## Key Takeaways
1. Mid-tenure, middle-aged customers with low balances and low credit scores are the most vulnerable to churn.  
2. Inactive customers churn far more than active ones → engagement programs are critical.  
3. Zero-balance customers are the largest churn group, but high-balance churners pose the biggest revenue risk.  
4. Geography and gender differences matter → churn prevention strategies should be tailored by demographic.  
5. Financial stability indicators (credit score, salary, balance) strongly correlate with churn.  

## Tools & Libraries
- **Python**  
- **pandas**  
- **numpy**  
- **matplotlib**  
- **seaborn**

## Dataset
- European Bank Customer Dataset (Unified Mentors Project)

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/bank-churn-analysis.git
   ```
2. Navigate to the project folder:
   ```bash
   cd bank-churn-analysis
   ```
3. Run the analysis script:
   ```bash
   python churn_analysis.py
   ```

## References
- Gupta, S., & Lehmann, D. R. (2003). Customers as assets. *Journal of Interactive Marketing*, 17(1), 9–24.  
- Verbeke, W., Martens, D., & Baesens, B. (2011). Social network analysis for customer churn prediction. *Applied Soft Computing*, 11(3), 221–230.  
- European Banking Authority (2024). Customer retention and risk management in EU banks. *Annual Report*.  
