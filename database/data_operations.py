import pandas as pd
from database.db_connection import get_connection


def insert_csv_to_db():

    df = pd.read_csv("dataset/sales_data.csv")

    conn = get_connection()

    df.to_sql(
        "sales",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()


def fetch_sales_data():

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM sales",
        conn
    )

    conn.close()

    return df


def fetch_total_revenue():

    conn = get_connection()

    query = """
    SELECT SUM(revenue)
    FROM sales
    """

    revenue = pd.read_sql_query(
        query,
        conn
    ).iloc[0, 0]

    conn.close()

    return revenue


def fetch_total_products():

    conn = get_connection()

    query = """
    SELECT COUNT(DISTINCT product_name)
    FROM sales
    """

    products = pd.read_sql_query(
        query,
        conn
    ).iloc[0, 0]

    conn.close()

    return products


def fetch_total_regions():

    conn = get_connection()

    query = """
    SELECT COUNT(DISTINCT region)
    FROM sales
    """

    regions = pd.read_sql_query(
        query,
        conn
    ).iloc[0, 0]

    conn.close()

    return regions