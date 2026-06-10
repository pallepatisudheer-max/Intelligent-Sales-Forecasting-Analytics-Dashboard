import pandas as pd
import os

def generate_excel_report(df):

    os.makedirs(
        "outputs/reports",
        exist_ok=True
    )

    output_file = (
        "outputs/reports/sales_report.xlsx"
    )

    df.to_excel(
        output_file,
        index=False
    )

    return output_file