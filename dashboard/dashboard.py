import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ===============================
# Page Configuration
# ===============================
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

st.title("📊 E-Commerce Business Dashboard")

# ===============================
# Load Data
# ===============================
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    return df

df = load_data()

# ===============================
# Sidebar Filter
# ===============================
st.sidebar.header("Filter")

selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(df['year'].unique())
)

filtered_df = df[df['year'] == selected_year]

# ===============================
# KPI Section
# ===============================
st.subheader("Business Overview Metrics")

total_revenue = filtered_df['revenue'].sum()
total_orders = filtered_df['order_id'].nunique()
total_customers = filtered_df['customer_unique_id'].nunique()
aov = filtered_df.groupby('order_id')['revenue'].sum().mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)
col4.metric("AOV", f"${aov:,.2f}")

# ===============================
# Monthly Revenue Trend
# ===============================
st.subheader("Monthly Revenue Trend")

monthly_revenue = filtered_df.groupby('month_year')['revenue'].sum()

fig, ax = plt.subplots()
monthly_revenue.plot(ax=ax)
plt.xticks(rotation=45)
plt.ylabel("Revenue")
st.pyplot(fig)

# ===============================
# Revenue by State
# ===============================
st.subheader("Top 10 States by Revenue")

state_revenue = (
    filtered_df.groupby('customer_state')['revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots()
state_revenue.plot(kind='bar', ax=ax)
plt.ylabel("Revenue")
st.pyplot(fig)

# ===============================
# Revenue by Category
# ===============================
st.subheader("Top 10 Categories by Revenue")

category_revenue = (
    filtered_df.groupby('product_category_name_english')['revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots()
category_revenue.plot(kind='bar', ax=ax)
plt.xticks(rotation=45)
plt.ylabel("Revenue")
st.pyplot(fig)

# ===============================
# Payment Behavior
# ===============================
st.subheader("Average Transaction Value by Payment Type")

payment_avg = (
    filtered_df.groupby('payment_type')['payment_value']
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots()
payment_avg.plot(kind='bar', ax=ax)
plt.ylabel("Average Payment Value")
st.pyplot(fig)

# ===============================
# Installment vs Transaction
# ===============================
st.subheader("Installment vs Average Payment Value")

installment_analysis = (
    filtered_df.groupby('payment_installments')['payment_value']
    .mean()
)

fig, ax = plt.subplots()
installment_analysis.plot(ax=ax)
plt.ylabel("Average Payment Value")
st.pyplot(fig)

# ===============================
# Footer
# ===============================
st.markdown("---")
st.markdown("Dashboard created using Streamlit")
