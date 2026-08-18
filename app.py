import streamlit as st

st.set_page_config(
    page_title="Customer Analytics & Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Analytics & Churn Prediction")
st.markdown("### E-commerce Customer Retention & Risk Analysis")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("High Risk Customers", "214")

with col2:
    st.metric("Medium Risk Customers", "119")

with col3:
    st.metric("Low Risk Customers", "530")

with col4:
    st.metric("High Risk Churn Rate", "91.12%")

st.divider()

st.header("Customer Risk Overview")

risk_data = {
    "Risk Level": ["High Risk", "Medium Risk", "Low Risk"],
    "Customers": [214, 119, 530],
    "Actual Churn Rate": ["91.12%", "72.27%", "1.13%"]
}

st.dataframe(
    risk_data,
    use_container_width=True,
    hide_index=True
)

st.header("Key Churn Drivers")

feature_data = {
    "Feature": [
        "RFM_Total",
        "Monetary",
        "Frequency",
        "Historical_CLV"
    ],
    "Importance": [
        "68.49%",
        "12.85%",
        "10.37%",
        "3.83%"
    ]
}

st.dataframe(
    feature_data,
    use_container_width=True,
    hide_index=True
)

st.info(
    "RFM_Total is the dominant predictive feature in the Gradient Boosting model."
)

st.header("Retention Strategy")

st.subheader("🔴 High Risk")
st.write("Prioritize immediate win-back campaigns, personalized offers and direct customer engagement.")

st.subheader("🟡 Medium Risk")
st.write("Use targeted re-engagement campaigns, product recommendations and limited-time offers.")

st.subheader("🟢 Low Risk")
st.write("Focus on loyalty, cross-selling, upselling and referral strategies.")
