import pandas as pd
from vincent.colors import brews
import win32com.client as win32
from pathlib import Path
from datetime import date
import random
import numpy as np
import pandas.io.sql as psql
import pypyodbc 

excel_file = 'FILE27.xlsx'
table = pd.read_excel(excel_file, sheetname="Prod_Data")
table = pd.pivot_table(df,index=['StartTime'],columns=['ProjectName','UserName'],values=['StartTime'],aggfunc='sum')
path='C:\\Users\\'
name='Report-{:%d-%m-%y}.xlsx'.format(date.today())
outputfile=path+name
sheet_name = 'Prod_Data'
sheet_name2='Log'
writer = pd.ExcelWriter(outputfile, engine='xlsxwriter')
table.to_excel(writer, sheet_name=sheet_name)
table.to_excel(writer,sheet_name='Log')
workbook = writer.book
worksheet = writer.sheets[sheet_name]
worksheet1 = writer.sheets[sheet_name2]
chart = workbook.add_chart({'type': 'column', 'subtype': 'stacked'})
for col_num in range(1, 30+ 1):
    chart.add_series({
        'name':       ['Sheet1', 0, col_num],
        'categories': ['Sheet1', 1, 0, 4, 0],
        'values':     ['Sheet1', 1, col_num, 4, col_num],
        'gap':        2,
    })
 
chart.set_y_axis({'major_gridlines': {'visible': False}})
worksheet.insert_chart('K2', chart)
writer.save()
