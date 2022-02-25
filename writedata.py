import openpyxl

path= "D:\job prep\sqa\write.xlsx"
workbook= openpyxl.load_workbook(path) #load the workbook from the path that is defined above
sheet= workbook.active  # or workbook.get_sheet_by_name("sheet1")

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r, column=c).value="welcome"

workbook.save(path)

