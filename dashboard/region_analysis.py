from database.data_operations import fetch_sales_data

def region_sales_analysis():

    df = fetch_sales_data()

    return (
        df.groupby("region")
        ["revenue"]
        .sum()
        .reset_index()
    )