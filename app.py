import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="E-Commerce Customer Intelligence",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
SQL_FILE = BASE_DIR / "sql" / "customer_analysis.sql"


# =========================================================
# DARK THEME
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #0b1120;
    color: #e5e7eb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background-color: #020617;
    border-right: 1px solid #1e293b;
}

section[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

/* Hero */

.hero {
    padding: 32px;
    border-radius: 20px;
    background: linear-gradient(135deg, #111827, #1e293b);
    border: 1px solid #334155;
    margin-bottom: 28px;
}

.hero h1 {
    color: #f8fafc !important;
    font-size: 40px;
    margin-bottom: 8px;
}

.hero p {
    color: #cbd5e1 !important;
    font-size: 17px;
}

/* Headings */

h1, h2, h3 {
    color: #f8fafc !important;
}

/* Text */

p, li {
    color: #cbd5e1;
}

/* Metric Cards */

div[data-testid="stMetric"] {
    background-color: #111827 !important;
    border: 1px solid #334155 !important;
    border-radius: 15px !important;
    padding: 20px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.25) !important;
}

div[data-testid="stMetric"] label {
    color: #94a3b8 !important;
}

div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    color: #f8fafc !important;
    font-size: 28px !important;
    font-weight: 700 !important;
}

div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {
    color: #cbd5e1 !important;
}

/* Tables */

div[data-testid="stDataFrame"] {
    border: 1px solid #334155;
    border-radius: 12px;
}

/* Selectbox */

div[data-baseweb="select"] > div {
    background-color: #111827 !important;
    border-color: #334155 !important;
    color: white !important;
}

/* Buttons */

.stButton > button {
    background-color: #2563eb;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
}

/* Alerts */

div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Footer */

.footer {
    text-align: center;
    color: #64748b;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# PLOTLY DARK THEME
# =========================================================

PLOTLY_LAYOUT = dict(
    paper_bgcolor="#111827",
    plot_bgcolor="#111827",
    font=dict(color="#e5e7eb"),
    title_font=dict(color="#f8fafc"),
    xaxis=dict(
        color="#cbd5e1",
        gridcolor="#334155"
    ),
    yaxis=dict(
        color="#cbd5e1",
        gridcolor="#334155"
    )
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🛍️ Customer Intelligence")

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Overview",
        "Customer Analytics",
        "Churn Prediction",
        "High-Risk Customers",
        "Power BI Dashboard",
        "SQL Analysis"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("### Project Stack")

st.sidebar.write("🐍 Python")
st.sidebar.write("🗄️ SQL")
st.sidebar.write("🤖 Machine Learning")
st.sidebar.write("📊 Power BI")
st.sidebar.write("🚀 Streamlit")

st.sidebar.divider()

st.sidebar.caption(
    "E-Commerce Customer Retention Project"
)


# =========================================================
# EXECUTIVE OVERVIEW
# =========================================================

if page == "Executive Overview":

    st.markdown("""
    <div class="hero">
        <h1>🛍️ E-Commerce Customer Intelligence</h1>
        <p>
        End-to-end customer analytics, retention and churn prediction system
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Total Customers", "4,314")

    with c2:
        st.metric("High-Risk Customers", "214")

    with c3:
        st.metric("Medium-Risk Customers", "119")

    with c4:
        st.metric("High-Risk Churn Rate", "91.12%")

    st.markdown("## 📊 Risk Overview")

    risk_data = pd.DataFrame({
        "Risk Level": [
            "Low Risk",
            "Medium Risk",
            "High Risk"
        ],
        "Customers": [
            530,
            119,
            214
        ],
        "Actual Churn Rate": [
            1.13,
            72.27,
            91.12
        ]
    })

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            risk_data,
            x="Risk Level",
            y="Customers",
            text="Customers",
            title="Customers by Risk Level"
        )

        fig.update_layout(**PLOTLY_LAYOUT)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        fig = px.bar(
            risk_data,
            x="Risk Level",
            y="Actual Churn Rate",
            text="Actual Churn Rate",
            title="Actual Churn Rate by Risk Level"
        )

        fig.update_layout(**PLOTLY_LAYOUT)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("## 💡 Key Business Findings")

    st.info(
        "RFM_Total is the dominant predictive feature, followed by "
        "Monetary and Frequency."
    )

    st.success(
        "High-risk customers should be prioritized for targeted "
        "retention and win-back campaigns."
    )


# =========================================================
# CUSTOMER ANALYTICS
# =========================================================

elif page == "Customer Analytics":

    st.title("📊 Customer Analytics")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Average Frequency", "5.26")

    with c2:
        st.metric("Average Monetary", "2,072.43")

    with c3:
        st.metric("Average Historical CLV", "2,081.18")

    st.markdown("## Customer Behaviour")

    behaviour = pd.DataFrame({
        "Feature": [
            "Frequency",
            "Monetary",
            "AOV",
            "Total Quantity",
            "Unique Products",
            "Purchase Span",
            "RFM Total",
            "Historical CLV"
        ],
        "Active": [
            5.26,
            2072.43,
            374.71,
            1367.93,
            75.86,
            179.48,
            10.01,
            2081.18
        ],
        "Churn": [
            2.13,
            684.27,
            340.85,
            428.96,
            35.74,
            57.38,
            5.56,
            688.20
        ]
    })

    feature = st.selectbox(
        "Select Behavioural Feature",
        behaviour["Feature"]
    )

    selected = behaviour[
        behaviour["Feature"] == feature
    ]

    chart_data = pd.DataFrame({
        "Customer Status": [
            "Active",
            "Churn"
        ],
        "Average": [
            selected["Active"].iloc[0],
            selected["Churn"].iloc[0]
        ]
    })

    fig = px.bar(
        chart_data,
        x="Customer Status",
        y="Average",
        text="Average",
        title=f"{feature}: Active vs Churn"
    )

    fig.update_layout(**PLOTLY_LAYOUT)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("## Behavioural Summary")

    st.dataframe(
        behaviour,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# CHURN PREDICTION
# =========================================================

elif page == "Churn Prediction":

    st.title("🤖 Churn Prediction")

    st.write(
        "Gradient Boosting based customer churn risk analysis."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Model", "Gradient Boosting")

    with c2:
        st.metric("RFM Importance", "68.49%")

    with c3:
        st.metric("High Risk", "214")

    with c4:
        st.metric("Medium Risk", "119")

    st.markdown("## 🔍 Top Predictive Features")

    importance = pd.DataFrame({
        "Feature": [
            "RFM_Total",
            "Monetary",
            "Frequency",
            "Historical_CLV"
        ],
        "Importance": [
            68.49,
            12.85,
            10.37,
            3.83
        ]
    })

    fig = px.bar(
        importance.sort_values("Importance"),
        x="Importance",
        y="Feature",
        orientation="h",
        text="Importance",
        title="Model Feature Importance"
    )

    fig.update_layout(**PLOTLY_LAYOUT)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("## ⚠️ Risk Distribution")

    risk_dist = pd.DataFrame({
        "Risk Level": [
            "Low Risk",
            "Medium Risk",
            "High Risk"
        ],
        "Customers": [
            530,
            119,
            214
        ]
    })

    fig = px.pie(
        risk_dist,
        names="Risk Level",
        values="Customers",
        hole=0.45,
        title="Customer Risk Distribution"
    )

    fig.update_layout(
        paper_bgcolor="#111827",
        font=dict(color="#e5e7eb"),
        title_font=dict(color="#f8fafc")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# HIGH-RISK CUSTOMERS
# =========================================================

elif page == "High-Risk Customers":

    st.title("🚨 High-Risk Customers")

    st.warning(
        "Prioritize these customers for retention and win-back campaigns."
    )

    high_risk = pd.DataFrame({
        "Customer ID": [
            16163,
            17345,
            15581,
            14654,
            13599,
            16887,
            15967,
            15984,
            13097,
            16329,
            12533,
            16620,
            15311,
            17377
        ],
        "Churn Probability (%)": [
            98.75,
            98.72,
            98.59,
            98.49,
            98.41,
            98.41,
            98.41,
            98.32,
            98.24,
            98.21,
            98.21,
            98.18,
            98.18,
            98.18
        ],
        "Risk Level": [
            "High Risk"
        ] * 14
    })

    st.dataframe(
        high_risk,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("## 🎯 Recommended Retention Actions")

    a1, a2, a3 = st.columns(3)

    with a1:

        st.markdown("### 🎯 Win-back")

        st.write(
            "Target inactive customers with personalized offers."
        )

    with a2:

        st.markdown("### 🛍️ Recommendations")

        st.write(
            "Use previous purchase behaviour for product recommendations."
        )

    with a3:

        st.markdown("### 💌 Engagement")

        st.write(
            "Use targeted email and promotional campaigns."
        )


# =========================================================
# JULIUS ANALYTICS DASHBOARD
# =========================================================

elif page == "Power BI Dashboard":

    st.title("📊 Interactive Analytics Dashboard")

    st.caption(
        "Interactive customer analytics dashboard powered by Julius"
    )

    st.divider()

    st.components.v1.iframe(
        "https://evanescent-pelican-ua4.julius.site/?utm_source=shared_artifact&ref=YPBE4QDHQADJ",
        height=900,
        scrolling=True
    )


# =========================================================
# SQL ANALYSIS
# =========================================================

elif page == "SQL Analysis":

    st.title("🗄️ SQL Analysis")

    st.markdown(
        "SQL was used as the analytical layer for revenue, "
        "customer behaviour, RFM segmentation, retention and churn analysis."
    )

    # -----------------------------------------------------
    # SQL KPIs
    # -----------------------------------------------------

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("SQL Queries", "59")

    with c2:
        st.metric("Analysis Areas", "6")

    with c3:
        st.metric("SQL Status", "Completed")

    st.divider()

    # -----------------------------------------------------
    # SQL ANALYSIS AREAS
    # -----------------------------------------------------

    st.markdown("## 📌 SQL Analysis Areas")

    sql_areas = pd.DataFrame({
        "Analysis": [
            "Revenue Analysis",
            "Customer Analysis",
            "RFM Segmentation",
            "Retention Analysis",
            "Churn Analysis",
            "Customer Behaviour"
        ],
        "Purpose": [
            "Analyse overall sales and revenue performance",
            "Understand customer purchasing behaviour",
            "Segment customers using RFM methodology",
            "Measure customer retention patterns",
            "Identify churn-related customer groups",
            "Analyse frequency, monetary value and purchases"
        ],
        "Status": [
            "Completed",
            "Completed",
            "Completed",
            "Completed",
            "Completed",
            "Completed"
        ]
    })

    st.dataframe(
        sql_areas,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # -----------------------------------------------------
    # ACTUAL SQL FILE
    # -----------------------------------------------------

    st.markdown("## 💻 SQL Query File")

    if SQL_FILE.exists():

        try:

            sql_code = SQL_FILE.read_text(
                encoding="utf-8"
            )

            st.code(
                sql_code,
                language="sql"
            )

        except Exception as e:

            st.error(
                f"Unable to read SQL file: {e}"
            )

    else:

        st.error(
            "SQL file not found."
        )

        st.caption(
            f"Expected location: {SQL_FILE}"
        )

    st.divider()

    st.success(
        "SQL analysis is integrated into the overall "
        "customer analytics workflow."
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown("""
<div class="footer">
E-Commerce Customer Intelligence
<br>
Python • SQL • Machine Learning • Power BI • Streamlit
</div>
""", unsafe_allow_html=True)