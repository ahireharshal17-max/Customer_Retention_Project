import streamlit as st
import pandas as pd

st.title("Customer Retention Analysis Dashboard")

df = pd.read_csv("Data/European_Bank.csv")

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

st.subheader("Churn by Number of Products")
products = pd.crosstab(df["NumOfProducts"], df["Exited"], normalize="index") * 100
st.bar_chart(products[1])

st.subheader("Disengaged Yet High-Value Customers")

high_value_customers = df[
    (df["Balance"] > df["Balance"].median()) &
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