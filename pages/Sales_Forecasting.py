import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

st.set_page_config(page_title="Sales Forecasting", layout="wide")

st.title("📈 Sales Forecasting")

# Load Model
model = joblib.load("models/sales_forecast_model.pkl")

st.subheader("🤖 Model Information")

c1, c2, c3 = st.columns(3)

c1.metric("Algorithm", "Linear Regression")
c2.metric("Model Status", "Trained")
c3.metric("Features", "3")

st.markdown("---")

st.subheader("📝 Enter Sales Details")

quantity = st.number_input(
    "Quantity",
    min_value=1,
    value=5
)

discount = st.number_input(
    "Discount",
    min_value=0.0,
    value=0.10
)

profit = st.number_input(
    "Profit",
    value=100.0
)

if st.button("🚀 Predict Sales"):

    input_df = pd.DataFrame({
        "Quantity": [quantity],
        "Discount": [discount],
        "Profit": [profit]
    })

    prediction = model.predict(input_df)

    predicted_sales = float(prediction[0])

    st.success(
        f"Predicted Sales: ${predicted_sales:.2f}"
    )

    st.markdown("---")

    st.subheader("📋 Prediction Details")

    result_df = pd.DataFrame({
        "Quantity": [quantity],
        "Discount": [discount],
        "Profit": [profit],
        "Predicted Sales": [predicted_sales]
    })

    st.dataframe(
        result_df,
        use_container_width=True
    )

    # Business Insights

    st.subheader("💡 Business Insights")

    if predicted_sales > 500:
        st.success("High Sales Expected")
    elif predicted_sales > 200:
        st.warning("Moderate Sales Expected")
    else:
        st.error("Low Sales Expected")

    st.markdown("---")

    # Forecast Future Months

    future_sales = [
        predicted_sales * 0.95,
        predicted_sales * 1.00,
        predicted_sales * 1.05,
        predicted_sales * 1.10,
        predicted_sales * 1.15
    ]

    forecast_df = pd.DataFrame({
        "Month": [
            "Month 1",
            "Month 2",
            "Month 3",
            "Month 4",
            "Month 5"
        ],
        "Forecast Sales": future_sales
    })

    growth = (
        (
            future_sales[-1] -
            future_sales[0]
        ) / future_sales[0]
    ) * 100

    st.subheader("📊 Forecast Dashboard")

    d1, d2, d3, d4 = st.columns(4)

    d1.metric(
        "Current Forecast",
        f"${predicted_sales:,.0f}"
    )

    d2.metric(
        "Maximum Forecast",
        f"${max(future_sales):,.0f}"
    )

    d3.metric(
        "Minimum Forecast",
        f"${min(future_sales):,.0f}"
    )

    d4.metric(
        "Growth %",
        f"{growth:.2f}%"
    )

    st.markdown("---")

    # Forecast Summary Chart

    st.subheader("📊 Forecast Summary")

    summary_df = pd.DataFrame({
        "Metric": [
            "Quantity",
            "Discount",
            "Profit",
            "Predicted Sales"
        ],
        "Value": [
            quantity,
            discount,
            profit,
            predicted_sales
        ]
    })

    fig_bar = px.bar(
        summary_df,
        x="Metric",
        y="Value",
        color="Metric",
        title="Forecast Metrics"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

    st.markdown("---")

    # Forecast Trend

    st.subheader("📈 Forecast Trend")

    fig_line = px.line(
        forecast_df,
        x="Month",
        y="Forecast Sales",
        markers=True,
        title="Future Sales Forecast"
    )

    st.plotly_chart(
        fig_line,
        use_container_width=True
    )

    st.markdown("---")

    # Pie Chart

    st.subheader("🥧 Current vs Future Sales")

    pie_df = pd.DataFrame({
        "Category": [
            "Current Sales",
            "Future Sales"
        ],
        "Value": [
            predicted_sales,
            future_sales[-1]
        ]
    })

    fig_pie = px.pie(
        pie_df,
        names="Category",
        values="Value",
        title="Current vs Future Sales"
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

    st.markdown("---")

    # Forecast Table

    st.subheader("📋 Forecast Table")

    forecast_df["Growth %"] = (
        forecast_df["Forecast Sales"]
        .pct_change()
        .fillna(0) * 100
    )

    st.dataframe(
        forecast_df,
        use_container_width=True
    )

    st.markdown("---")

    # Download Forecast

    csv = forecast_df.to_csv(
        index=False
    )

    st.download_button(
        "⬇ Download Forecast CSV",
        csv,
        file_name="forecast_report.csv",
        mime="text/csv"
    )