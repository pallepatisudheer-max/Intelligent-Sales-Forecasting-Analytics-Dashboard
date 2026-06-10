import pandas as pd
import numpy as np


def prepare_inventory_data(df):

    np.random.seed(42)

    df["inventory_level"] = np.random.randint(
        20, 150, len(df)
    )

    df["reorder_point"] = (
        df["Quantity"] * 3
    )

    df["stock_status"] = np.where(
        df["inventory_level"] < df["reorder_point"],
        "Reorder Needed",
        "Healthy Stock"
    )

    df["safety_stock"] = (
        df["Quantity"] * 1.5
    )

    df["reorder_quantity"] = (
        df["reorder_point"] - df["inventory_level"]
    )

    df["reorder_quantity"] = (
        df["reorder_quantity"].clip(lower=0)
    )

    return df


def get_low_stock(df):

    return df[
        df["stock_status"] == "Reorder Needed"
    ]


def get_top_inventory(df):

    return (
        df.sort_values(
            by="inventory_level",
            ascending=False
        ).head(10)
    )


def calculate_safety_stock(df):

    df["safety_stock"] = (
        df["Quantity"] * 1.5
    )

    return df


def calculate_reorder_quantity(df):

    df["reorder_quantity"] = (
        df["reorder_point"]
        - df["inventory_level"]
    )

    df["reorder_quantity"] = (
        df["reorder_quantity"].clip(lower=0)
    )

    return df


def get_inventory_summary(df):

    return {
        "total_products": len(df),
        "average_inventory": int(
            df["inventory_level"].mean()
        ),
        "low_stock_products": int(
            (
                df["stock_status"]
                == "Reorder Needed"
            ).sum()
        ),
        "healthy_stock": int(
            (
                df["stock_status"]
                == "Healthy Stock"
            ).sum()
        ),
        "highest_inventory": int(
            df["inventory_level"].max()
        ),
        "lowest_inventory": int(
            df["inventory_level"].min()
        )
    }