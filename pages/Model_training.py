import streamlit as st
import pandas as pd
import numpy as np
import joblib

import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

st.title("🤖 Model Training")

# =========================
# LOAD DATA
# =========================

df = pd.read_csv("dataset/sales_data.csv", encoding="latin1")

st.success("Dataset Loaded Successfully")

# =========================
# FEATURES
# =========================

X = df[[
    "Quantity",
    "Discount",
    "Profit"
]]

y = df["Sales"]

# =========================
# SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

st.success("Data Split Successfully")

# =========================
# TRAIN MODEL
# =========================

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

st.success("Model Trained Successfully")

# =========================
# PREDICTIONS
# =========================

predictions = model.predict(X_test)

# =========================
# METRICS
# =========================

mae = mean_absolute_error(
    y_test,
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        predictions
    )
)

r2 = r2_score(
    y_test,
    predictions
)

# =========================
# KPI CARDS
# =========================

st.subheader("Model Performance")

c1, c2, c3 = st.columns(3)

c1.metric(
    "MAE",
    f"{mae:.2f}"
)

c2.metric(
    "RMSE",
    f"{rmse:.2f}"
)

c3.metric(
    "R² Score",
    f"{r2:.4f}"
)

# =========================
# MODEL SUMMARY
# =========================

st.subheader("Dataset Summary")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Rows", len(df))
c2.metric("Features", len(X.columns))
c3.metric("Train Rows", len(X_train))
c4.metric("Test Rows", len(X_test))

# =========================
# METRICS TABLE
# =========================

st.subheader("Metrics Table")

metrics_df = pd.DataFrame({
    "Metric": [
        "MAE",
        "RMSE",
        "R² Score"
    ],
    "Value": [
        mae,
        rmse,
        r2
    ]
})

st.dataframe(
    metrics_df,
    use_container_width=True
)

# =========================
# ACTUAL VS PREDICTED
# =========================

st.subheader("Actual vs Predicted")

results = pd.DataFrame({
    "Actual Sales": y_test.values,
    "Predicted Sales": predictions
})

st.dataframe(
    results.head(50),
    use_container_width=True
)

# =========================
# SCATTER CHART
# =========================

st.subheader("Actual vs Predicted Sales")

fig = px.scatter(
    results,
    x="Actual Sales",
    y="Predicted Sales",
    title="Actual vs Predicted"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# RESIDUAL ANALYSIS
# =========================

st.subheader("Residual Analysis")

results["Residual"] = (
    results["Actual Sales"]
    - results["Predicted Sales"]
)

fig = px.histogram(
    results,
    x="Residual",
    nbins=40,
    title="Residual Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# ERROR TREND
# =========================

st.subheader("Prediction Error Trend")

fig = px.line(
    results.head(200),
    y="Residual",
    title="Prediction Error Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# FEATURE IMPORTANCE
# =========================

st.subheader("Feature Importance")

importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

st.dataframe(
    importance,
    use_container_width=True
)

# BAR CHART

fig = px.bar(
    importance,
    x="Feature",
    y="Coefficient",
    title="Feature Importance"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# PIE CHART

fig = px.pie(
    importance,
    names="Feature",
    values="Coefficient",
    title="Feature Contribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# CORRELATION HEATMAP
# =========================

st.subheader("Correlation Heatmap")

corr_cols = [
    "Sales",
    "Profit",
    "Quantity",
    "Discount"
]

fig, ax = plt.subplots(
    figsize=(8,5)
)

sns.heatmap(
    df[corr_cols].corr(),
    annot=True,
    cmap="Blues",
    ax=ax
)

st.pyplot(fig)

# =========================
# SALES VS PROFIT
# =========================

st.subheader("Sales vs Profit")

fig = px.scatter(
    df,
    x="Sales",
    y="Profit",
    color="Category",
    hover_name="Product Name"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================
# TOP SALES
# =========================

st.subheader("Top 10 Highest Sales")

top_sales = df.nlargest(
    10,
    "Sales"
)

st.dataframe(
    top_sales,
    use_container_width=True
)

# =========================
# TRAIN DATA
# =========================

st.subheader("Training Dataset Preview")

st.dataframe(
    X_train.head(20),
    use_container_width=True
)

# =========================
# TEST DATA
# =========================

st.subheader("Testing Dataset Preview")

st.dataframe(
    X_test.head(20),
    use_container_width=True
)

# =========================
# SAVE MODEL
# =========================

joblib.dump(
    model,
    "models/sales_forecast_model.pkl"
)

st.success("Model Saved Successfully")