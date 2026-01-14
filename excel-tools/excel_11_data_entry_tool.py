from openpyxl import Workbook

def create_excel(data):
    wb = Workbook()
    ws = wb.active
    for row in data:
        ws.append(row)
    wb.save('data.xlsx')
    print("Excel file created successfully!")

data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Anna", 25, "London"],
]

create_excel(data)