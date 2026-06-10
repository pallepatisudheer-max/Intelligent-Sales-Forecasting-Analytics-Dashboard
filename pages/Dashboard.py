import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main {
    padding-top: 0.5rem;
}

.metric-card {
    background: #111827;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #374151;
}

.metric-title {
    color: #9CA3AF;
    font-size: 14px;
}

.metric-value {
    color: #60A5FA;
    font-size: 28px;
    font-weight: bold;
}

.hero {
    background: linear-gradient(135deg,#0f172a,#1e293b);
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(
    "dataset/sales_data.csv",
    encoding="latin1"
)

df["Order Date"] = pd.to_datetime(
    df["Order Date"]
)

# =====================================
# HERO SECTION
# =====================================

st.markdown("""
<div class="hero">

<h1>🚀 AI Sales Analytics Dashboard</h1>

<h4>
Intelligent Sales Forecasting &
Inventory Optimization Platform
</h4>

</div>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR FILTERS
# =====================================

st.sidebar.header("🔍 Filters")

selected_region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["Category"].isin(selected_category))
]

# =====================================
# KPI CALCULATIONS
# =====================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = len(filtered_df)

total_customers = (
    filtered_df["Customer ID"]
    .nunique()
)

# =====================================
# KPI CARDS
# =====================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Total Sales",
        f"${total_sales:,.0f}"
    )

with col2:
    st.metric(
        "📈 Total Profit",
        f"${total_profit:,.0f}"
    )

with col3:
    st.metric(
        "🛒 Total Orders",
        f"{total_orders:,}"
    )

with col4:
    st.metric(
        "👥 Customers",
        total_customers
    )

st.markdown("---")

# =====================================
# MONTHLY SALES TREND
# =====================================

monthly_sales = (
    filtered_df
    .groupby(
        filtered_df["Order Date"]
        .dt.to_period("M")
    )["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order Date"] = (
    monthly_sales["Order Date"]
    .astype(str)
)

st.subheader("📈 Monthly Sales Trend")

fig1 = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.markdown("---")
# =====================================
# CATEGORY & REGION ANALYSIS
# =====================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("📦 Sales by Category")

    category_sales = (
        filtered_df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    fig2 = px.bar(
        category_sales,
        x="Category",
        y="Sales",
        color="Category",
        title="Category Performance"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

with col2:

    st.subheader("🌍 Sales by Region")

    region_sales = (
        filtered_df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    fig3 = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        hole=0.5
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

st.markdown("---")

# =====================================
# SEGMENT ANALYSIS
# =====================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("👥 Customer Segments")

    segment_sales = (
        filtered_df.groupby("Segment")["Sales"]
        .sum()
        .reset_index()
    )

    fig4 = px.bar(
        segment_sales,
        x="Segment",
        y="Sales",
        color="Segment"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

with col2:

    st.subheader("🚚 Ship Mode Analysis")

    ship_sales = (
        filtered_df.groupby("Ship Mode")["Sales"]
        .sum()
        .reset_index()
    )

    fig5 = px.pie(
        ship_sales,
        names="Ship Mode",
        values="Sales"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

st.markdown("---")

# =====================================
# TOP PRODUCTS
# =====================================

st.subheader("🏆 Top 10 Products")

top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig6 = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top Selling Products"
)

st.plotly_chart(
    fig6,
    use_container_width=True
)

st.dataframe(
    top_products,
    use_container_width=True
)

st.markdown("---")

# =====================================
# MONTHLY PROFIT TREND
# =====================================

monthly_profit = (
    filtered_df
    .groupby(
        filtered_df["Order Date"]
        .dt.to_period("M")
    )["Profit"]
    .sum()
    .reset_index()
)

monthly_profit["Order Date"] = (
    monthly_profit["Order Date"]
    .astype(str)
)

st.subheader("📈 Monthly Profit Trend")

fig7 = px.line(
    monthly_profit,
    x="Order Date",
    y="Profit",
    markers=True,
    title="Profit Trend"
)

st.plotly_chart(
    fig7,
    use_container_width=True
)

st.markdown("---")

# =====================================
# BUSINESS INSIGHTS
# =====================================

st.subheader("💡 Executive Summary")

highest_category = (
    category_sales
    .sort_values("Sales", ascending=False)
    .iloc[0]["Category"]
)

highest_region = (
    region_sales
    .sort_values("Sales", ascending=False)
    .iloc[0]["Region"]
)

st.success(f"🏆 Best Performing Category: {highest_category}")

st.success(f"🌍 Best Performing Region: {highest_region}")

st.info(
    f"""
Revenue Generated: ${total_sales:,.0f}

Profit Generated: ${total_profit:,.0f}

Orders Processed: {total_orders:,}

Customers Served: {total_customers}
"""
)

st.markdown("---")

# =====================================
# RECENT TRANSACTIONS
# =====================================

st.subheader("📋 Recent Transactions")

st.dataframe(
    filtered_df[
        [
            "Order Date",
            "Customer Name",
            "Category",
            "Sales",
            "Profit"
        ]
    ].tail(20),
    use_container_width=True
)