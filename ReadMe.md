'''
# Food Suggestion With NLP Analysis

## Project Overview
This project develops a food-based recommendation system designed to improve health outcomes by analyzing both past datasets and current 2025 real-time data.  
The system focuses on key health indicators such as BMI, diet patterns, and exercise levels to provide personalized, data-driven food suggestions.  

The college nutrition website used for data collection was built by my friends, while I handled the backend, data analysis, NLP processing, and visualization.  
The main goal is to help both business users and customers make informed decisions about nutrition through insights generated from structured and unstructured data.

---

## My Role and Contributions
- Managed the entire backend and data analysis workflow.  
- Collected real-time data from the college website and combined it with past historical datasets.  
- Cleaned and verified all datasets using Excel Power Query and Python.  
- Applied NLP techniques to analyze community conversations related to food and fitness.  
- Built interactive Power BI dashboards for business and customer insights.

---

## Overall Project Workflow

### 1. Data Collection
- Data Sources:
  - Real-time 2025 data gathered from the college nutrition website (built by my teammates).  
  - Historical and global food-impact datasets used for reference and trend comparison.  
- Tools Used:
  - MySQL for database management.  
  - Python (mysql.connector) for data extraction and CSV export.  

---

### 2. Data Cleaning and Preparation
- Excel Power Query used for:
  - Removing duplicates and null values.  
  - Standardizing numeric and categorical data.  
  - Structuring tables for consistency across years.  
- Python (Pandas, NumPy) used for:
  - Data validation and correlation checks.  
  - Ensuring correct data types and integrity.

**Techniques & Algorithms:**
- Missing Value Imputation  
- Outlier Detection  
- Pearson Correlation Coefficient (for numeric relationship analysis)

---

### 3. Natural Language Processing (NLP)
Applied NLP to community chat data to understand diet and fitness discussions.

**Steps & Algorithms Used:**
1. Tokenization – Split text into individual words.  
2. Stopword Removal – Eliminate common non-informative words.  
3. Text Cleaning – Remove punctuation, symbols, and noise using Regex.  
4. Negation Handling – Detect negation terms like *not*, *never* to correctly interpret sentiment.  
5. Sentiment Analysis –  
   - Rule-based approach using positive/negative word lists.  
   - TextBlob polarity method for cross-validation.  
6. Workout vs Diet Classification – Categorized messages using keyword matching.  
7. Topic Extraction – Identify common themes like weight loss, protein diet, healthy lifestyle, etc.

---

### 4. Data Verification and Integration
- Combined past data with current 2025 website data for future-driven insights.  
- Checked data consistency, shape, and datatypes using df.info() and df.corr().  
- Validated text-based sentiment patterns with structured health records.

---

### 5. Visualization and Reporting
Created interactive dashboards using Power BI to visualize both historical and real-time data.

**Key Insights Displayed:**
- BMI and weight trends over time.  
- Sentiment distribution (positive, negative, neutral).  
- Diet vs Workout discussion frequencies.  
- Regional and gender-based health behavior patterns.  

**Reports Generated:**
- Business Reports: For company stakeholders to make strategic decisions.  
- Customer Recommendations: Personalized food and lifestyle suggestions.

---

## Tools and Technologies

| Stage | Tools / Libraries | Key Techniques / Algorithms |
|-------|--------------------|-----------------------------|
| Data Collection | MySQL, Python (mysql.connector) | SQL Querying, CSV Export |
| Data Cleaning | Excel Power Query, Pandas, NumPy | Missing Value Imputation, Correlation Analysis |
| NLP Processing | NLTK, TextBlob, Regex | Tokenization, Stopword Removal, Sentiment Analysis, Negation Handling |
| Integration | Pandas, MySQL | Data Merging, Schema Alignment |
| Visualization | Power BI | Trend Analysis, Filtering, Interactive Dashboards |
| Environment | Anaconda, VS Code | Full Backend Data Workflow |

---

## Final Outcome
By combining past data and current 2025 website data, this project delivers:  
- Accurate, data-driven reports for business decision-makers.  
- Personalized recommendations for customers based on their BMI, diet type, and behavior.  
- A unified system that transforms raw data into actionable insights for real-time health improvement.  

This end-to-end solution demonstrates the integration of Excel, MySQL, Python (NLP), and Power BI to create a complete data analytics pipeline supporting a full-stack nutrition website.
'''
