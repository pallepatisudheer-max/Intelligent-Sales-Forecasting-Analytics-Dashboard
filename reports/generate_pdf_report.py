from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import os


def generate_pdf_report(df):

    os.makedirs(
        "outputs/reports",
        exist_ok=True
    )

    pdf_path = (
        "outputs/reports/sales_report.pdf"
    )

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Sales Analytics Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"Total Revenue : ${df['Sales'].sum():,.2f}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Total Profit : ${df['Profit'].sum():,.2f}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Total Orders : {len(df)}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Products Sold : {int(df['Quantity'].sum())}",
            styles["BodyText"]
        )
    )

    doc.build(content)

    return pdf_path