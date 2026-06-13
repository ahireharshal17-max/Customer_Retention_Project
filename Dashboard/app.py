import streamlit as st
import pandas as pd

st.title("Customer Retention Analysis Dashboard")

df = pd.read_csv("Data/European_Bank.csv")
st.sidebar.header("Filters")

balance_threshold = st.sidebar.slider(
    "Balance Threshold",
    0,
    int(df["Balance"].max()),
    int(df["Balance"].median())
)

st.subheader("Dataset Preview") 
st.dataframe(df.head())

st.subheader("Customer Churn Distribution")
st.bar_chart(df["Exited"].value_counts())

st.subheader("Churn by Geography")
geo = pd.crosstab(df["Geography"], df["Exited"], normalize="index") * 100
st.bar_chart(geo[1])

st.subheader("Churn by Active Membership")
active = pd.crosstab(df["IsActiveMember"], df["Exited"], normalize="index") * 100
st.bar_chart(active[1]) 
st.subheader("Churn by Gender")
gender = pd.crosstab(df["Gender"], df["Exited"], normalize="index") * 100
st.bar_chart(gender[1])

st.subheader("Product Utilization Impact Analysis")
st.write(
    "Customers with 2 products show the lowest churn rate, while customers with 3 or more products show significantly higher churn."
)
products = pd.crosstab(df["NumOfProducts"], df["Exited"], normalize="index") * 100
st.bar_chart(products[1])

st.subheader("Disengaged Yet High-Value Customers")

high_value_customers = df[
    (df["Balance"] > balance_threshold) &
    (df["IsActiveMember"] == 0)
]

st.write(
    f"Number of disengaged high-value customers: {len(high_value_customers)}"
)

st.dataframe(
    high_value_customers[
        ["CustomerId", "Balance", "EstimatedSalary", "IsActiveMember", "Exited"]
    ].head(10)
)
st.subheader("Retention Strength Scoring Panel")

df["RelationshipStrength"] = (
    df["IsActiveMember"] +
    (df["NumOfProducts"] >= 2).astype(int)
)

relationship = pd.crosstab(
    df["RelationshipStrength"],
    df["Exited"],
    normalize="index"
) * 100

st.bar_chart(relationship[1])