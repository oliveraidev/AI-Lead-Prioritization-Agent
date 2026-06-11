import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Lead Prioritization Agent",
    layout="wide"
)

st.title("AI-Powered Lead Prioritization Agent")

st.write("Predicting customer conversion probability and prioritizing sales leads.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("ROC AUC", "0.78")

with col2:
    st.metric("Accuracy", "0.89")

with col3:
    st.metric("Top 100 Successes", "83")

st.subheader("Business Objective")
st.write(
    "This dashboard helps sales teams identify which leads should be contacted first under limited call capacity."
)

st.subheader("Top Priority Leads")

import pandas as pd

leads = pd.read_csv("data/top_leads.csv")

leads["Recommended Action"] = "Call immediately"

st.dataframe(
    leads.head(20),
    use_container_width=True
)
st.subheader("Top Feature Importance")

feature_importance = pd.DataFrame({
    "Feature": [
        "balance",
        "age",
        "day",
        "campaign",
        "poutcome_success",
        "pdays"
    ],
    "Importance": [
        0.26,
        0.23,
        0.18,
        0.11,
        0.08,
        0.07
    ]
})

st.bar_chart(
    feature_importance.set_index("Feature")
)