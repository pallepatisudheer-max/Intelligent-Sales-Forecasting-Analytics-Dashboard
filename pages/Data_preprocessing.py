import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Data Preprocessing",
    layout="wide"
)

st.title("🧹 Data Preprocessing")

try:
    df = pd.read_csv(
        "dataset/sales_data.csv",
        encoding="latin1"
    )

except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# Dataset Information

st.subheader("📌 Dataset Information")

st.write(
    f"Rows: {df.shape[0]} | Columns: {df.shape[1]}"
)

st.markdown("---")

# Missing Values

st.subheader("❌ Missing Values")

missing_values = (
    df.isnull()
    .sum()
    .reset_index()
)

missing_values.columns = [
    "Column",
    "Missing Values"
]

st.dataframe(
    missing_values,
    use_container_width=True
)

fig1 = px.bar(
    missing_values,
    x="Column",
    y="Missing Values",
    title="Missing Values Analysis"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.markdown("---")

# Remove Missing Values

df_clean = df.dropna()

# Cleaned Dataset

st.subheader("🧹 Cleaned Dataset")

st.dataframe(
    df_clean.head(20),
    use_container_width=True
)

st.markdown("---")

# Sales by Category

st.subheader("💰 Sales by Category")

category_sales = (
    df_clean.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    title="Total Sales by Category"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# Profit by Category

st.subheader("📈 Profit by Category")

category_profit = (
    df_clean.groupby("Category")["Profit"]
    .sum()
    .reset_index()
)

fig3 = px.bar(
    category_profit,
    x="Category",
    y="Profit",
    color="Category",
    title="Total Profit by Category"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# Sales Distribution

st.subheader("📊 Sales Distribution")

fig4 = px.histogram(
    df_clean,
    x="Sales",
    nbins=40,
    title="Sales Distribution"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# Profit Distribution

st.subheader("📉 Profit Distribution")

fig5 = px.box(
    df_clean,
    y="Profit",
    title="Profit Distribution"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# Save Processed Dataset

df_clean.to_csv(
    "dataset/processed_sales_data.csv",
    index=False
)

st.success(
    "✅ Processed dataset saved successfully!"
)