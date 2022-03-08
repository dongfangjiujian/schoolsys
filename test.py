# from docx import Document
# from docx.shared import Cm
# document=Document('12.docx')
# tables=document.tables
# print(len(tables))
# table=tables[1]
# cells=table._cells
# print(len(cells))
# cells_string=[cell.text for cell in cells]
# # print(cells_string)
# col_num= len(table.columns)
# print(col_num)
# row_num=len(table.rows)
# print(row_num)

# row0=table.rows[0]
# col0=table.columns[7]

# row0_str=[cell.text for cell in row0.cells]
# print(row0_str)
# col0_str=[cell.text for cell in col0.cells]
# print(col0_str)
# print(table.cell(0,7).text)
# pic=table.cell(0,6)
# run=pic.paragraphs[0].add_run()
# run.add_picture('docs/aassddff.jpg',width=Cm(2.5))

# document.save('12.docx')
from datetime import datetime,date,time

print(datetime.now())
print(date.today())