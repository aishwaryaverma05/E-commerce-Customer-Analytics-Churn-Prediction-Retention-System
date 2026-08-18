# 🛒 E-Commerce Customer Analytics, Churn Prediction & Retention System

An end-to-end **customer analytics and churn prediction system** built to transform e-commerce transaction data into actionable customer, revenue, retention, and churn insights.

The project combines **data cleaning, exploratory data analysis, SQL analytics, RFM segmentation, cohort analysis, Customer Lifetime Value (CLV), machine learning, churn-risk identification, customer recommendations, and an interactive Streamlit dashboard** in a single analytics workflow.

<p align="center">
  <a href="https://e-commerce-customer-analytics-churn-prediction-retention-syste.streamlit.app/">
    <strong> Live Interactive Dashboard</strong>
  </a>
</p>

---

## 📌 Project Overview

E-commerce businesses generate large volumes of customer and transaction data, but raw transactional data alone does not explain:

* Which customers are most valuable?
* Which customers are becoming inactive?
* Which customers are at high risk of churn?
* How do customer segments behave over time?
* How well are customers being retained?
* Which customers should receive targeted retention actions?

This project addresses these questions by combining **descriptive analytics, customer segmentation, SQL-based analysis, predictive modeling, and interactive visualization**.

The final outcome is a dashboard that allows users to move from **high-level business performance → customer behavior → churn risk → actionable retention analysis**.

---

## 🎯 Business Objectives

The project focuses on five major objectives:

1. **Understand customer behavior**

   * Analyze purchasing patterns and customer activity.
   * Identify valuable and inactive customer segments.

2. **Segment customers**

   * Use RFM analysis to classify customers based on:

     * Recency
     * Frequency
     * Monetary value

3. **Measure customer retention**

   * Analyze customer cohorts and retention patterns over time.

4. **Predict churn risk**

   * Build a machine learning workflow to identify customers who may be at risk of churning.

5. **Support retention decisions**

   * Combine customer value, behavior, and churn risk to help prioritize retention efforts.

---

## 📊 Dashboard Modules

The Streamlit application contains six major analytical areas.

### 1. 🏠 Executive Overview

Provides a high-level view of the e-commerce business and customer base.

Key focus areas include:

* Business KPIs
* Customer activity
* Revenue trends
* Overall customer behavior
* High-level performance indicators

---

### 2. 👥 Customer Analytics

Explores customer behavior and segmentation.

Key analysis includes:

* Customer purchasing behavior
* RFM segmentation
* Customer value
* Spending patterns
* Customer-level analytics

The goal is to understand **who the customers are and how they behave**.

---

### 3. 🤖 Churn Prediction

Uses machine learning to estimate customer churn risk.

The workflow includes:

* Feature preparation
* Customer-level feature engineering
* Model training
* Churn prediction
* Risk classification
* Prediction-driven customer analysis

The objective is not only to identify churn, but to help businesses **prioritize customers who may require retention attention**.

---

### 4. 🚨 High-Risk Customers

Focuses specifically on customers identified as higher-risk.

This section helps answer:

* Who is at higher churn risk?
* Which customers should be prioritized?
* What customer characteristics are associated with higher risk?
* How can customer-level insights support retention actions?

This converts model output into a more practical **retention-focused customer view**.

---

### 5. 📈 Interactive Analytics Dashboard

Provides interactive exploration of customer and business data.

Users can investigate patterns through:

* Interactive charts
* Customer segments
* Trends
* Filters
* Comparative analysis
* Behavioral insights

The purpose is to allow users to explore the data rather than relying only on static reports.

---

### 6. 🗄️ SQL Analysis

Demonstrates the SQL-based analytical layer of the project.

The SQL section contains analysis areas covering customer and transaction-level business questions.

It provides visibility into the underlying analytical queries used to derive business insights.

---

## 🔍 Analytical Framework

The project follows an end-to-end analytics workflow:

```text
Raw E-Commerce Data
        ↓
Data Cleaning & Preparation
        ↓
Exploratory Data Analysis
        ↓
SQL Business Analysis
        ↓
Customer-Level Feature Engineering
        ↓
RFM Segmentation
        ↓
Cohort Analysis
        ↓
Customer Lifetime Value
        ↓
Churn Prediction
        ↓
High-Risk Customer Identification
        ↓
Retention Insights & Recommendations
        ↓
Interactive Streamlit Dashboard
```

---

## 📐 RFM Customer Segmentation

RFM analysis is used to understand customer value and engagement.

### Recency

Measures how recently a customer made a purchase.

**Lower recency → more recent activity**

### Frequency

Measures how often a customer purchases.

**Higher frequency → stronger purchasing engagement**

### Monetary

Measures how much a customer spends.

**Higher monetary value → higher customer value**

Combining these dimensions allows customers to be grouped into meaningful behavioral segments and supports targeted retention strategies.

---

## 📅 Cohort Analysis

Cohort analysis is used to evaluate customer retention over time.

Customers are grouped based on their initial purchase period and then tracked across subsequent periods.

This helps answer questions such as:

* How well are customers retained after their first purchase?
* Which cohorts demonstrate stronger retention?
* Where does customer activity decline?
* How does retention change over the customer lifecycle?

---

## 💰 Customer Lifetime Value

Customer Lifetime Value (CLV) is incorporated to understand the economic value of customers.

Instead of treating every customer equally, CLV helps identify customers who may have greater long-term business importance.

This becomes particularly useful when combined with churn risk:

```text
High Customer Value + High Churn Risk
                ↓
       High Retention Priority
```

This combination provides a stronger basis for retention prioritization than churn probability alone.

---

## 🧠 Churn Prediction

The machine learning component is designed to identify customers who may be at risk of churn based on customer-level behavioral features.

The modeling workflow includes:

1. Customer-level feature preparation
2. Feature engineering
3. Model training
4. Prediction
5. Churn-risk classification
6. Customer prioritization

The model output is then integrated into the Streamlit dashboard so that predictive analytics can be explored alongside descriptive customer analytics.

> **Important:** Churn predictions should be treated as decision-support signals rather than absolute predictions. In a production environment, model monitoring, retraining, validation, and business context would be required.

---

## 🗄️ SQL Analysis

SQL is used as an analytical layer for answering business questions from transactional/customer data.

The project includes a dedicated `sql/` directory containing the SQL analysis.

Examples of analytical questions include:

* Customer purchase behavior
* Revenue and transaction analysis
* Customer-level aggregation
* Repeat purchasing behavior
* Customer segmentation
* Business performance analysis

The SQL analysis is also surfaced directly within the Streamlit application for transparency and demonstration purposes.

---

## 💡 Business Use Cases

The system can support decisions such as:

### 🎯 Retention Campaigns

Prioritize customers with:

* High churn risk
* High customer value
* Declining engagement

### 💎 VIP Customer Management

Identify customers with:

* High frequency
* High monetary value
* Strong long-term value

### 🔄 Re-Engagement

Identify customers showing:

* Increasing recency
* Reduced purchasing frequency
* Lower engagement

### 📣 Targeted Marketing

Use customer segments to create more relevant campaigns instead of treating the entire customer base uniformly.

---

## 🛠️ Tech Stack

| Technology       | Purpose                                                |
| ---------------- | ------------------------------------------------------ |
| **Python**       | Data analysis, feature engineering & application logic |
| **Pandas**       | Data manipulation and analysis                         |
| **NumPy**        | Numerical operations                                   |
| **Scikit-learn** | Machine learning and predictive modeling               |
| **SQL**          | Business and customer analytics                        |
| **Streamlit**    | Interactive web application                            |
| **Plotly**       | Interactive data visualization                         |
| **Git & GitHub** | Version control and project management                 |

---

## 📁 Project Structure

```text
E-commerce-Customer-Analytics-Churn-Prediction-Retention-System/
│
├── app.py
│
├── sql/
│   └── SQL analysis queries
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Live Demo

Explore the deployed Streamlit application:

**[Open the Live Dashboard](https://e-commerce-customer-analytics-churn-prediction-retention-syste.streamlit.app/)**

The live application allows users to interact with the project's customer analytics, churn prediction, high-risk customer analysis, interactive analytics, and SQL analysis sections.

---

## 💻 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/aishwaryaverma05/E-commerce-Customer-Analytics-Churn-Prediction-Retention-System.git
```

### 2. Navigate into the project

```bash
cd E-commerce-Customer-Analytics-Churn-Prediction-Retention-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

## 📈 Key Skills Demonstrated

This project demonstrates practical experience across several areas of data analytics and data science.

### Data Analytics

* Data cleaning
* Exploratory data analysis
* Customer analytics
* KPI analysis
* Trend analysis

### SQL

* Business-oriented SQL analysis
* Customer-level aggregation
* Transaction analysis
* Analytical query development

### Customer Analytics

* RFM segmentation
* Cohort analysis
* Customer Lifetime Value
* Customer behavior analysis
* Customer prioritization

### Machine Learning

* Feature engineering
* Churn prediction
* Customer risk classification
* Predictive analytics

### Data Visualization

* Interactive dashboards
* Business-focused visualizations
* Customer segmentation views
* Risk analysis

### Deployment

* Streamlit application development
* GitHub-based project management
* Cloud deployment

---

## 📊 From Analytics to Action

A major goal of this project is to move beyond simply reporting metrics.

The workflow connects:

```text
Customer Behavior
       +
Customer Value
       +
Churn Risk
       ↓
Retention Priority
       ↓
Targeted Business Action
```

This makes the project more closely aligned with how customer analytics can be used in real-world business decision-making.

---

## ⚠️ Limitations

This project is designed as an end-to-end analytics and portfolio application.

For production deployment, additional capabilities would be required, including:

* Automated data pipelines
* Scheduled model retraining
* Model monitoring
* Drift detection
* Production-grade data validation
* Secure data storage
* Authentication and authorization
* Experimentation / A-B testing
* Integration with CRM or marketing platforms

Therefore, the churn predictions should be interpreted as **analytical decision-support outputs**, not guaranteed customer outcomes.

---

## 🔮 Future Improvements

Potential extensions include:

* Automated model retraining pipelines
* Advanced hyperparameter optimization
* Explainable AI / SHAP-based churn explanations
* Customer-level retention recommendations
* Marketing campaign integration
* Real-time customer risk scoring
* Automated reporting
* Model monitoring and drift detection
* Customer segmentation using additional behavioral features
* A/B testing for retention strategies

---

## 👩‍💻 Author

**Aishwarya Verma**

Data Analytics | Business Intelligence | Machine Learning

### Project Links

* **GitHub:** [E-Commerce Customer Analytics, Churn Prediction & Retention System](https://github.com/aishwaryaverma05/E-commerce-Customer-Analytics-Churn-Prediction-Retention-System)
* **Live Dashboard:** [Streamlit Application](https://e-commerce-customer-analytics-churn-prediction-retention-syste.streamlit.app/)

---

## ⭐ Project Summary

This project demonstrates how **SQL, Python, customer analytics, machine learning, and interactive dashboards** can be combined to build an end-to-end customer retention analytics solution.

It transforms raw customer and transaction data into a decision-support workflow covering:

**Analyze → Segment → Predict → Prioritize → Retain**

---

⭐ If you found this project useful, consider giving the repository a star.
