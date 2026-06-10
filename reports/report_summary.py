from database.data_operations import (
    fetch_total_revenue,
    fetch_total_products,
    fetch_total_regions
)

def generate_summary():

    return {
        "Total Revenue": fetch_total_revenue(),
        "Total Products": fetch_total_products(),
        "Total Regions": fetch_total_regions()
    }