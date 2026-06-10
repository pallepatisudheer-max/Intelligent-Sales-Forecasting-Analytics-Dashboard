def create_features(df):

    df["avg_price"] = (
        df["revenue"] /
        df["quantity_sold"]
    )

    return df