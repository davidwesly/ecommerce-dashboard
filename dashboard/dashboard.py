import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    return df

df = load_data()

# =============================
# SIDEBAR FILTER
# =============================

st.sidebar.header("Filter")

min_date = df['order_purchase_timestamp'].min()
max_date = df['order_purchase_timestamp'].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

selected_states = st.sidebar.multiselect(
    "Select State",
    options=df['customer_state'].unique(),
    default=df['customer_state'].unique()
)

# Apply filters
filtered_df = df[
    (df['order_purchase_timestamp'].dt.date >= date_range[0]) &
    (df['order_purchase_timestamp'].dt.date <= date_range[1]) &
    (df['customer_state'].isin(selected_states))
]

# =============================
# KPI SECTION
# =============================

total_revenue = filtered_df['revenue'].sum()
total_orders = filtered_df['order_id'].nunique()
total_customers = filtered_df['customer_unique_id'].nunique()
aov = total_revenue / total_orders if total_orders > 0 else 0

st.title("📊 E-Commerce Business Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"{total_revenue:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Total Customers", total_customers)
col4.metric("Average Order Value", f"{aov:,.2f}")

st.markdown("---")

# =============================
# MONTHLY REVENUE TREND
# =============================

st.subheader("📈 Monthly Revenue Trend")

monthly_revenue = filtered_df.groupby(
    filtered_df['order_purchase_timestamp'].dt.to_period('M')
)['revenue'].sum()

monthly_revenue.index = monthly_revenue.index.astype(str)

fig1, ax1 = plt.subplots(figsize=(10,5))
ax1.plot(monthly_revenue.index, monthly_revenue.values)
ax1.set_xticklabels(monthly_revenue.index, rotation=90)
ax1.set_ylabel("Revenue")

st.pyplot(fig1)

# =============================
# MONTHLY ORDER TREND
# =============================

st.subheader("📦 Monthly Order Trend")

monthly_orders = filtered_df.groupby(
    filtered_df['order_purchase_timestamp'].dt.to_period('M')
)['order_id'].nunique()

monthly_orders.index = monthly_orders.index.astype(str)

fig2, ax2 = plt.subplots(figsize=(10,5))
ax2.plot(monthly_orders.index, monthly_orders.values)
ax2.set_xticklabels(monthly_orders.index, rotation=90)
ax2.set_ylabel("Orders")

st.pyplot(fig2)

st.markdown("---")

# =============================
# REVENUE BY STATE
# =============================

st.subheader("🌍 Revenue by State")

state_revenue = filtered_df.groupby('customer_state')['revenue'].sum().sort_values(ascending=False).head(10)

fig3, ax3 = plt.subplots(figsize=(8,5))
state_revenue.plot(kind='bar', ax=ax3)
ax3.set_ylabel("Revenue")

st.pyplot(fig3)

st.markdown("---")

# =============================
# TOP PRODUCT CATEGORY
# =============================

st.subheader("📦 Top 10 Product Categories")

category_revenue = filtered_df.groupby('product_category_name_english')['revenue'].sum().sort_values(ascending=False).head(10)

fig4, ax4 = plt.subplots(figsize=(10,5))
category_revenue.plot(kind='bar', ax=ax4)
ax4.set_ylabel("Revenue")
ax4.set_xticklabels(category_revenue.index, rotation=45)

st.pyplot(fig4)

st.markdown("---")

# =============================
# RFM SEGMENT DISTRIBUTION
# =============================

st.subheader("👥 Customer Segment Distribution")

# Recalculate RFM quickly inside dashboard
snapshot_date = filtered_df['order_purchase_timestamp'].max() + pd.Timedelta(days=1)

rfm = filtered_df.groupby('customer_unique_id').agg({
    'order_purchase_timestamp': lambda x: (snapshot_date - x.max()).days,
    'order_id': 'nunique',
    'revenue': 'sum'
}).reset_index()

rfm.columns = ['customer_id','Recency','Frequency','Monetary']

rfm['R_score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1]).astype(int)
rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5]).astype(int)
rfm['M_score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5]).astype(int)

def segment_customer(row):
    if row['R_score'] == 5 and row['F_score'] >= 4:
        return 'Champions'
    elif row['F_score'] >= 4:
        return 'Loyal Customers'
    elif row['M_score'] == 5:
        return 'Big Spenders'
    elif row['R_score'] <= 2:
        return 'At Risk'
    else:
        return 'Potential'

rfm['Segment'] = rfm.apply(segment_customer, axis=1)

segment_counts = rfm['Segment'].value_counts()

fig5, ax5 = plt.subplots(figsize=(8,5))
segment_counts.plot(kind='bar', ax=ax5)
ax5.set_ylabel("Number of Customers")


st.pyplot(fig5)

