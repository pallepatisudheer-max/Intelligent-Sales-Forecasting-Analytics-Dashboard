from database.data_operations import (
    fetch_total_revenue,
    fetch_total_products,
    fetch_total_regions
)

def get_kpis():

    return {
        "revenue": fetch_total_revenue(),
        "products": fetch_total_products(),
        "regions": fetch_total_regions()
    }