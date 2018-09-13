import xlsxwriter

workbook = xlsxwriter.Workbook('Expenses02.xlsx')
worksheet = workbook.add_worksheet()

# add bold format
bold = workbook.add_format({'bold':True})
# add number format
money = workbook.add_format({'num_format':'$#,##0'})

worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)

expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

row = 1
col = 0

for item, cost in (expenses):
    worksheet.write(row, col, item)
    worksheet.write(row, col+1, cost, money)
    row += 1

# Add Formulas
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()