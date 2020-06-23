from datetime import datetime
import xlwt

style_header = xlwt.easyxf('align : horz centre, vert centre')
style_legend_right = xlwt.easyxf('font : bold 1; align : horz right;')
style_legend_center = xlwt.easyxf('font : bold 1; align : horz centre;')
style_core_columns = xlwt.easyxf('font : bold 1, color white;\
    align : horz centre;\
    pattern: pattern solid, fore_color black;')
border = xlwt.easyxf('borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin;')
border_center = xlwt.easyxf('borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin;\
    align : horz centre;')
border_right = xlwt.easyxf('borders: top_color black, bottom_color black, right_color black, left_color black, left thin, right thin, top thin, bottom thin;\
    align : horz right;')

workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('January')

# Initialize current row and column
row = 0
col = 0
sheet1.row(0).height = 1000
sheet1.col(1).width = 5000

# Header
sheet1.write_merge(row, row, col, col + 1, 'Will be Decided', style_header)
col += 2
sheet1.write_merge(row, row, col, col + 4, 'Class : TBD', style_header)
col += 5
sheet1.write_merge(row, row, col, col + 7, 'Training Officer : TBD', style_header)

# Legend
row += 2
col = 1
sheet1.write(row, col, 'LEGEND :', style_legend_center)
col += 1
sheet1.write(row, col, 'LO : ', style_legend_right)
col += 1
sheet1.write(row, col, 'Letter of Excuse')
col += 3
sheet1.write(row, col, 'MO : ', style_legend_right)
col += 1
sheet1.write(row, col, 'Medical Certificate')
col += 3
sheet1.write(row, col, 'E : ', style_legend_right)
col += 1
sheet1.write(row, col, 'Early Dismissal')
col += 3
sheet1.write(row, col, 'O : ', style_legend_right)
col += 1
sheet1.write(row, col, 'Reason for absence not provided')

# Core columns : No, Client Name, Days of month (1 to n), Percentage
row += 1
col = 0
sheet1.write(row, col, 'No', style_core_columns)
sheet1.col(col).width = (len('No') + 2) * 256
col += 1
sheet1.write(row, col, 'Client\'s Name', style_core_columns)

for day in range(1, 31):
    col += 1
    sheet1.write(row, col, day, style_core_columns)
    sheet1.col(col).width = 1500

col += 1
sheet1.write(row, col, '%', style_core_columns)
sheet1.col(col).width = 1500

row += 1
### This section will be contain list of students name and their attendee status ###
row += 1
col = 2
# Total Actual attendance
sheet1.write_merge(row, row, 0, 1, 'Total Actual Attendance', border_right)
row += 1

# Total Possible attendance
sheet1.write_merge(row, row, 0, 1, 'Total Possible attendance', border_right)

# Footer checked by
row += 2
sheet1.write(row, 24, 'Checked by:')
row += 1
sheet1.write(row, 26, 'Tess Domingo (DAC Executive)')

# Save file to excel
workbook.save('example-1.xls')