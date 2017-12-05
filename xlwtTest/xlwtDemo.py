# coding:utf-8
'''
    Author:minning
    Date:2017/10/18
    代码目的：xlwt的基本使用
    
'''

import xlwt

file = xlwt.Workbook()
table = file.add_sheet('sheet01',cell_overwrite_ok=True)
table.write(0,0,'1A')
file.save('demo.xls')

