import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="EDA Analysis",
    layout="wide"
)

st.title("📊 Exploratory Data Analysis")

# Load Dataset
df = pd.read_csv(
    "dataset/sales_data.csv",
    encoding="latin1"
)

# -----------------------------
# KPI CARDS
# -----------------------------
st.subheader("Dataset Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])
col3.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col4.metric("Total Profit", f"${df['Profit'].sum():,.0f}")

st.divider()

# -----------------------------
# DATA PREVIEW
# -----------------------------
st.subheader("Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

# -----------------------------
# MISSING VALUES
# -----------------------------
st.subheader("Missing Values Analysis")

missing_values = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values
})

st.dataframe(
    missing_values,
    use_container_width=True
)

# -----------------------------
# SALES DISTRIBUTION
# -----------------------------
st.subheader("Sales Distribution")

fig = px.histogram(
    df,
    x="Sales",
    nbins=50,
    title="Sales Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# PROFIT DISTRIBUTION
# -----------------------------
st.subheader("Profit Distribution")

fig = px.histogram(
    df,
    x="Profit",
    nbins=50,
    title="Profit Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# CATEGORY ANALYSIS
# -----------------------------
st.subheader("Category Analysis")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig = px.pie(
    category_sales,
    names="Category",
    values="Sales",
    title="Sales by Category"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# REGION ANALYSIS
# -----------------------------
st.subheader("Region Analysis")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    color="Region",
    title="Sales by Region"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# SEGMENT ANALYSIS
# -----------------------------
st.subheader("Customer Segment Analysis")

segment_sales = (
    df.groupby("Segment")["Sales"]
    .sum()
    .reset_index()
)

fig = px.pie(
    segment_sales,
    names="Segment",
    values="Sales",
    title="Sales by Customer Segment"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# SHIP MODE ANALYSIS
# -----------------------------
st.subheader("Ship Mode Analysis")

ship_mode_sales = (
    df.groupby("Ship Mode")["Sales"]
    .sum()
    .reset_index()
)

fig = px.bar(
    ship_mode_sales,
    x="Ship Mode",
    y="Sales",
    color="Ship Mode",
    title="Sales by Ship Mode"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# TOP PRODUCTS
# -----------------------------
st.subheader("Top 10 Products")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# TOP CUSTOMERS
# -----------------------------
st.subheader("Top 10 Customers")

top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig = px.bar(
    top_customers,
    x="Sales",
    y="Customer Name",
    orientation="h",
    title="Top 10 Customers"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# STATE ANALYSIS
# -----------------------------
st.subheader("Top States by Sales")

state_sales = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(15)
    .reset_index()
)

fig = px.bar(
    state_sales,
    x="State",
    y="Sales",
    color="State",
    title="Top States by Sales"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# CORRELATION ANALYSIS
# -----------------------------
st.subheader("Correlation Matrix")

corr = df[
    ["Sales", "Profit", "Quantity", "Discount"]
].corr()

st.dataframe(
    corr,
    use_container_width=True
)

# -----------------------------
# STATISTICAL SUMMARY
# -----------------------------
st.subheader("Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True
)