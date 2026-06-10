from database.data_operations import fetch_sales_data

def inventory_data():

    df = fetch_sales_data()

    return df[
        [
            "product_name",
            "inventory_level"
        ]
    ]