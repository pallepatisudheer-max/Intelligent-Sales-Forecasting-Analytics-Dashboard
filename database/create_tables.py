from database.db_connection import get_connection


def create_sales_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_date TEXT,
            product_name TEXT,
            category TEXT,
            region TEXT,
            quantity_sold INTEGER,
            unit_price REAL,
            revenue REAL,
            inventory_level INTEGER
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_sales_table()
    print("Sales table created successfully")