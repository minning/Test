# coding:utf-8
'''
    Author:minning
    Date:2017/10/18
    代码目的：测试xlrd的使用
    
'''
import xlrd


excelfile = r'excelfile.xlsx'
data = xlrd.open_workbook(excelfile)
table = data.sheets()[0]
print table
nrows = table.nrows
ncols = table.ncols
print nrows
print ncols
ncols = table.ncols
for i in range(nrows):
    print table.row_values(i)
    # for rowItem in table.row_values(i):
    #     print rowItem
linebreak = "*"*20
print linebreak
print table.col_values(0)
print linebreak
for j in range(ncols):
    print table.col_values(j)
    # for colsItem in table.col_values(i):
    #     print colsItem

row = 0
col = 0
ctype = 1
value = 'new_1a'
xf = 0
table.put_cell(row,col,ctype,value,xf)
print table.cell(0,0)
