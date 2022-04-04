from openpyxl import Workbook
wb = Workbook()
ws = wb.active
#ws['A1'] = "RCV Academy"

testdata = [['Name', 'City'],['Juan', 'Mendoza'],['Leila', 'Dorrego'],['Pedro', 'Cordoba']]
for data in testdata:
    ws.append(data)
wb.save("demoexcel.xlsx")

