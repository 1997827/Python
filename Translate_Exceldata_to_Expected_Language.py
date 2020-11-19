import sys
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from translate import Translator
import xlwt 
from xlwt import Workbook 


wb = Workbook() 
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet1')   
program_name = sys.argv 
df = pd.read_excel(program_name, sheetname='Sheet1')
print(df.columns)
for index, row in df.iterrows():
    print (row[0])
    val=row[0]
    translator= Translator(to_lang="zh-tw")    
    translation = translator.translate(val)
    a= translation
    print(a)
    sheet1.write(1, 0,a) 
    wb.save('example.xls') 
