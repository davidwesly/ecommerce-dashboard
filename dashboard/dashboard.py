import streamlit as st
import pandas as pd

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="E-Commerce Business Dashboard",
    layout="wide"
)

st.title("📊 E-Commerce Business Dashboard")

# ==================================================
# LOAD DATA
# ==================================================
@st.cache_data
def load_data():
    return pd.read_csv("dashboard/main_data.csv")

df = load_data()

# ==================================================
# SIDEBAR FILTER
# ==================================================
st.sidebar.header("Filter Data")

selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(df['year'].unique())
)

filtered_df = df[df['year'] == selected_year]

# ==================================================
# KPI SECTION
# ==================================================
st.subheader("📌 Business Overview Metrics")

total_revenue = filtered_df['revenue'].sum()
total_orders = filtered_df['order_id'].nunique()
total_customers = filtered_df['customer_unique_id'].nunique()
aov = filtered_df.groupby('order_id')['revenue'].sum().mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Total Customers", f"{total_customers:,}")
col4.metric("Average Order Value", f"${aov:,.2f}")

# ==================================================
# MONTHLY REVENUE TREND
# ==================================================
st.subheader("📈 Monthly Revenue Trend")

monthly_revenue = (
    filtered_df.groupby('month_year')['revenue']
    .sum()
    .sort_index()
)

st.line_chart(monthly_revenue)

# ==================================================
# TOP 10 STATES
# ==================================================
st.subheader("🏙️ Top 10 States by Revenue")

state_revenue = (
    filtered_df.groupby('customer_state')['revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(state_revenue)

# ==================================================
# TOP 10 CATEGORIES
# ==================================================
st.subheader("🛍️ Top 10 Categories by Revenue")

category_revenue = (
    filtered_df.groupby('product_category_name_english')['revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(category_revenue)

# ==================================================
# PAYMENT ANALYSIS
# ==================================================
st.subheader("💳 Average Revenue by Payment Type")

payment_avg = (
    filtered_df.groupby('payment_type')['revenue']
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(payment_avg)

# ==================================================
# INSTALLMENT ANALYSIS
# ==================================================
st.subheader("📊 Installment vs Average Revenue")

installment_analysis = (
    filtered_df.groupby('payment_installments')['revenue']
    .mean()
    .sort_index()
)

st.line_chart(installment_analysis)

# ==================================================
# FOOTER
# ==================================================
st.markdown("---")
st.markdown("Dashboard created using Streamlit 🚀")
