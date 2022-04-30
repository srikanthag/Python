import xlrd

f_path = r"C:\Users\srikanth\Desktop\IT\Python\python_practice\_python\file_handling\excel\student.xlsx"

#working the book
xl_obj = xlrd.open_workbook(f_path)
#opening the spread sheet and getting its handle
xl_sheet = xl_obj.sheet_by_name("marks_sheet")

#getting all rows in sheet as generator object
data = xl_sheet.get_rows()

#skipping header
header = next(data)

#traversing through each row
for row in data:
    print(row[0].value, row[1].value)













