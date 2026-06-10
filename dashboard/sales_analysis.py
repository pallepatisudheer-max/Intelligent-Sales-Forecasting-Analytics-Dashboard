from database.data_operations import fetch_sales_data

def product_sales_analysis():

    df = fetch_sales_data()

    return (
        df.groupby("product_name")
        ["revenue"]
        .sum()
        .reset_index()
    )