# Vendor Performance Analysis | Retail Inventory & Sales  

_Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using SQL, Python, and Power BI._  

---

## 📑 Table of Contents  
- [Overview](#overview)  
- [Business Problem](#business-problem)  
- [Dataset](#dataset)  
- [Tools & Technologies](#tools--technologies)  
- [Project Structure](#project-structure)  
- [Data Cleaning & Preparation](#data-cleaning--preparation)  
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)  
- [Research Questions & Key Findings](#research-questions--key-findings)  
- [Dashboard](#dashboard)  
- [How to Run This Project](#how-to-run-this-project)  
- [Final Recommendations](#final-recommendations)  
- [Author & Contact](#author--contact)  

---

## 📌 Overview  
This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for purchasing, pricing, and inventory optimization.  
A complete data pipeline was built using **SQL** for ETL, **Python** for analysis and hypothesis testing, and **Power BI** for visualization.  

---

## 💡 Business Problem  
Effective inventory and sales management are critical in the retail sector. This project aims to:  
- Identify underperforming brands needing pricing or promotional adjustments.  
- Determine vendor contributions to sales and profits.  
- Support decision-making in procurement and sourcing.  

---

## 📊 Dataset  
- **Source:** Retail sales & inventory transactions.  
- **Size:** ~100K records (CSV/SQL).  
- **Key Columns:** VendorName, Brand, PurchasePrice, SalesPrice, Quantity, ProfitMargin, etc.  

---

## 🛠 Tools & Technologies  
- **SQL (PostgreSQL)** – ETL, data aggregation, complex queries.  
- **Python (Pandas, NumPy, Matplotlib, Seaborn, Statsmodels)** – Data cleaning, EDA, hypothesis testing.  
- **Power BI** – Dashboard & visualization.  
- **Git/GitHub** – Version control.  

---

## 📂 Project Structure  
```plaintext
├── data/                 # Raw & cleaned datasets  
├── notebooks/            # Jupyter notebooks (EDA, modeling)  
├── scripts/              # SQL queries & Python scripts  
├── dashboard/            # Power BI file  
└── README.md             # Project documentation  
---

🧹 Data Cleaning & Preparation

- Handled missing values and outliers.
- Ensured compliance with data dictionaries.
- Applied transformations for consistency.
---
🔎 Exploratory Data Analysis (EDA)

- Distribution analysis of profit margins & sales.
- Vendor performance comparisons.
- Inventory turnover insights.
---
❓ Research Questions & Key Findings

- Is vendor profitability significantly different between top vs low performers?
- What percentage of purchases are concentrated in the top 10 vendors?
- How does bulk purchasing affect overall cost savings?
---
Key Insights:

- Top 10 vendors contribute 65.7% of purchases.
- Over $2.71M in unsold inventory tied to underperforming vendors.
- Bulk purchasing yields up to 72% cost savings.
---
📊 Dashboard

- Power BI dashboard provides:
- Vendor performance KPIs.
- Profit margin trends.
- Inventory optimization insights.
---
▶ How to Run This Project

Clone the repository:

 git clone https://github.com/username/repo-name.git

- Import SQL scripts to set up database.
- Run Python notebooks for data cleaning & analysis.
- Open Power BI file for interactive dashboard.
---
✅ Final Recommendations

- Diversify vendor base to reduce dependency.
- Optimize inventory by reducing slow-moving items.
- Leverage bulk purchasing strategies for cost efficiency.
---
👤 Author & Contact

Abhijeet Kumar Pandey

- Email: abhijeet.kr.pandey.07@gmail.com
- LinkedIn: linkedin.com/in/abhitech07
- GitHub: github.com/abhitech07





























