import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    df = pd.read_csv("main_data.csv")
    return df

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

fig1, ax1 = plt.subplots()
monthly_revenue.plot(ax=ax1)
ax1.set_ylabel("Revenue")
ax1.tick_params(axis='x', rotation=45)

st.pyplot(fig1)

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

fig2, ax2 = plt.subplots()
state_revenue.plot(kind='bar', ax=ax2)
ax2.set_ylabel("Revenue")

st.pyplot(fig2)

# ==================================================
# TOP 10 PRODUCT CATEGORIES
# ==================================================
st.subheader("🛍️ Top 10 Categories by Revenue")

category_revenue = (
    filtered_df.groupby('product_category_name_english')['revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig3, ax3 = plt.subplots()
category_revenue.plot(kind='bar', ax=ax3)
ax3.set_ylabel("Revenue")
ax3.tick_params(axis='x', rotation=45)

st.pyplot(fig3)

# ==================================================
# PAYMENT METHOD ANALYSIS
# ==================================================
st.subheader("💳 Average Revenue by Payment Type")

payment_avg = (
    filtered_df.groupby('payment_type')['revenue']
    .mean()
    .sort_values(ascending=False)
)

fig4, ax4 = plt.subplots()
payment_avg.plot(kind='bar', ax=ax4)
ax4.set_ylabel("Average Revenue")

st.pyplot(fig4)

# ==================================================
# INSTALLMENT ANALYSIS
# ==================================================
st.subheader("📊 Installment vs Average Revenue")

installment_analysis = (
    filtered_df.groupby('payment_installments')['revenue']
    .mean()
    .sort_index()
)

fig5, ax5 = plt.subplots()
installment_analysis.plot(ax=ax5)
ax5.set_ylabel("Average Revenue")

st.pyplot(fig5)

# ==================================================
# FOOTER
# ==================================================
st.markdown("---")
st.markdown("Dashboard created using Streamlit 🚀")
