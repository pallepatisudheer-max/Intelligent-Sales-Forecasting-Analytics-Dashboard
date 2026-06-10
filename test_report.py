from reports.generate_excel_report import (
    generate_excel_report
)

file_path = generate_excel_report()

print(
    "Report Generated:",
    file_path
)