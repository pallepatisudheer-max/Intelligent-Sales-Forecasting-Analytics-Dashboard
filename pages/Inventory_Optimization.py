import streamlit as st
import pandas as pd
import plotly.express as px

from inventory.inventory_optimizer import (
    prepare_inventory_data,
    get_low_stock,
    get_top_inventory,
    get_inventory_summary
)

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Inventory Optimization",
    layout="wide"
)

st.title("📦 Inventory Optimization Dashboard")

# =====================================
# LOAD DATASET
# =====================================

try:
    df = pd.read_csv(
        "dataset/sales_data.csv",
        encoding="latin1"
    )

except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# =====================================
# PREPARE INVENTORY DATA
# =====================================

df = prepare_inventory_data(df)

summary = get_inventory_summary(df)

# =====================================
# KPI CARDS
# =====================================

st.subheader("📊 Inventory Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Products",
        summary["total_products"]
    )

with col2:
    st.metric(
        "Average Inventory",
        summary["average_inventory"]
    )

with col3:
    st.metric(
        "Low Stock Products",
        summary["low_stock_products"]
    )

with col4:
    st.metric(
        "Healthy Stock",
        summary["healthy_stock"]
    )

st.markdown("---")

# =====================================
# INVENTORY DISTRIBUTION
# =====================================

st.subheader("📈 Inventory Distribution")

fig1 = px.histogram(
    df,
    x="inventory_level",
    nbins=20,
    title="Inventory Level Distribution"
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# =====================================
# STOCK STATUS
# =====================================

st.subheader("🥧 Stock Status")

status_df = (
    df["stock_status"]
    .value_counts()
    .reset_index()
)

status_df.columns = [
    "Status",
    "Count"
]

fig2 = px.pie(
    status_df,
    names="Status",
    values="Count",
    title="Stock Status Distribution"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# =====================================
# CATEGORY INVENTORY
# =====================================

st.subheader("📦 Inventory by Category")

category_inventory = (
    df.groupby("Category")["inventory_level"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    category_inventory,
    x="Category",
    y="inventory_level",
    color="Category",
    title="Average Inventory by Category"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# =====================================
# REGION INVENTORY
# =====================================

st.subheader("🌍 Inventory by Region")

region_inventory = (
    df.groupby("Region")["inventory_level"]
    .mean()
    .reset_index()
)

fig4 = px.bar(
    region_inventory,
    x="Region",
    y="inventory_level",
    color="Region",
    title="Average Inventory by Region"
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# =====================================
# LOW STOCK ALERTS
# =====================================

st.subheader("🚨 Low Stock Alerts")

low_stock = get_low_stock(df)

if not low_stock.empty:

    st.dataframe(
        low_stock[
            [
                "Product Name",
                "Category",
                "Region",
                "Quantity",
                "inventory_level",
                "reorder_point",
                "reorder_quantity"
            ]
        ],
        use_container_width=True
    )

else:

    st.success(
        "✅ No Products Need Reordering"
    )

st.markdown("---")

# =====================================
# TOP INVENTORY PRODUCTS
# =====================================

st.subheader("🏆 Top Inventory Products")

top_inventory = get_top_inventory(df)

st.dataframe(
    top_inventory[
        [
            "Product Name",
            "Category",
            "inventory_level"
        ]
    ],
    use_container_width=True
)

fig5 = px.bar(
    top_inventory,
    x="Product Name",
    y="inventory_level",
    color="inventory_level",
    title="Top Inventory Products"
)

st.plotly_chart(
    fig5,
    use_container_width=True
)

# =====================================
# BUSINESS INSIGHTS
# =====================================

st.subheader("💡 Business Insights")

st.info(
    f"""
Total Products: {summary['total_products']}

Low Stock Products: {summary['low_stock_products']}

Average Inventory: {summary['average_inventory']}

Highest Inventory: {summary['highest_inventory']}

Lowest Inventory: {summary['lowest_inventory']}
"""
)

# =====================================
# DATASET PREVIEW
# =====================================

st.subheader("🗂 Dataset Preview")

st.dataframe(
    df.head(100),
    use_container_width=True
)

st.success(
    "✅ Inventory Optimization Completed Successfully"
)