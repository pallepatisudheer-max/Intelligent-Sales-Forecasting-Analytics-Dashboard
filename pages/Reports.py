import streamlit as st
import pandas as pd
import plotly.express as px

from reports.generate_excel_report import generate_excel_report
from reports.generate_pdf_report import generate_pdf_report

st.set_page_config(
    page_title="Reports",
    layout="wide"
)

st.title("📄 Sales Reports & Analytics")

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv(
    "dataset/sales_data.csv",
    encoding="latin1"
)

# =========================
# KPI CARDS
# =========================

st.subheader("📊 Business Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Revenue",
    f"${df['Sales'].sum():,.0f}"
)

col2.metric(
    "Total Profit",
    f"${df['Profit'].sum():,.0f}"
)

col3.metric(
    "Total Orders",
    len(df)
)

col4.metric(
    "Products Sold",
    int(df["Quantity"].sum())
)

st.markdown("---")

# =========================
# SUMMARY TABLE
# =========================

st.subheader("📋 Sales Statistics")

summary_df = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Profit",
        "Average Revenue",
        "Average Profit",
        "Total Orders"
    ],
    "Value": [
        df["Sales"].sum(),
        df["Profit"].sum(),
        df["Sales"].mean(),
        df["Profit"].mean(),
        len(df)
    ]
})

st.dataframe(
    summary_df,
    use_container_width=True
)

st.markdown("---")

# =========================
# CATEGORY SALES
# =========================

st.subheader("📦 Sales by Category")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    title="Revenue by Category"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =========================
# REGION SALES
# =========================

st.subheader("🌍 Sales by Region")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Sales Distribution by Region"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

# =========================
# TOP PRODUCTS
# =========================

st.subheader("🏆 Top 10 Products")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(
    top_products.reset_index(),
    use_container_width=True
)

st.markdown("---")

# =========================
# DATASET PREVIEW
# =========================

st.subheader("🗂 Dataset Preview")

st.dataframe(
    df.head(100),
    use_container_width=True
)

st.markdown("---")

# =========================
# DOWNLOAD REPORTS
# =========================

st.subheader("⬇ Download Reports")

try:

    excel_path = generate_excel_report(df)

except:

    excel_path = "outputs/reports/sales_report.xlsx"

try:

    pdf_path = generate_pdf_report()

except:

    pdf_path = "outputs/reports/sales_report.pdf"

with open(excel_path, "rb") as file:

    st.download_button(
        label="📊 Download Excel Report",
        data=file,
        file_name="sales_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key="excel_download"
    )

with open(pdf_path, "rb") as file:

    st.download_button(
        label="📄 Download PDF Report",
        data=file,
        file_name="sales_report.pdf",
        mime="application/pdf",
        key="pdf_download"
    )

st.success("✅ Excel & PDF Reports Ready")