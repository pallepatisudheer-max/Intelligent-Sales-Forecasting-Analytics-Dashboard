from database.data_operations import (
    fetch_sales_data,
    fetch_total_revenue,
    fetch_total_products,
    fetch_total_regions
)

print(fetch_sales_data().head())

print("Revenue:", fetch_total_revenue())

print("Products:", fetch_total_products())
print("Regions:", fetch_total_regions())