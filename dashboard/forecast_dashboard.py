from database.data_operations import fetch_sales_data

def revenue_trend():

    df = fetch_sales_data()

    trend = (
        df.groupby("order_date")
        ["revenue"]
        .sum()
        .reset_index()
    )

    return trend