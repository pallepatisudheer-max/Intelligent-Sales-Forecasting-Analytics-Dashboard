import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Data Upload",
    layout="wide"
)

st.title("📂 Data Upload")

try:
    df = pd.read_csv(
        "dataset/sales_data.csv",
        encoding="latin1"
    )

    st.success("Dataset Loaded Successfully!")

except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# Dataset Info

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.markdown("---")

# Dataset Preview

st.subheader("📋 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.markdown("---")

# Category Distribution

st.subheader("📊 Products by Category")

category_count = (
    df["Category"]
    .value_counts()
    .reset_index()
)

category_count.columns = [
    "Category",
    "Count"
]

fig1 = px.bar(
    category_count,
    x="Category",
    y="Count",
    color="Category",
    title="Products by Category"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# Region Distribution

st.subheader("🌍 Sales by Region")

region_count = (
    df["Region"]
    .value_counts()
    .reset_index()
)

region_count.columns = [
    "Region",
    "Count"
]

fig2 = px.pie(
    region_count,
    names="Region",
    values="Count",
    title="Region Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# Segment Distribution

st.subheader("👥 Customer Segments")

segment_count = (
    df["Segment"]
    .value_counts()
    .reset_index()
)

segment_count.columns = [
    "Segment",
    "Count"
]

fig3 = px.bar(
    segment_count,
    x="Segment",
    y="Count",
    color="Segment",
    title="Customer Segments"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.success("✅ Data Upload Completed")