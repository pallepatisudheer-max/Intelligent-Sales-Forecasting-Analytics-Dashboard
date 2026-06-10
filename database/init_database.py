from database.create_tables import create_sales_table
from database.data_operations import insert_sales_data

create_sales_table()

insert_sales_data(
    "dataset/sales_data.csv"
)

print("Database Initialized Successfully")