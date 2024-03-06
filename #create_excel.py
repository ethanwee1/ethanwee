#create_excel
import sqlite3
import pandas as pd

con = sqlite3.connect('unittest.db')
wb = pd.read_excel('new_PyTorch_OSS_unittest_trend.xlsx',sheet_name = None)


for sheet in wb:

    wb[sheet].to_sql(sheet,con,index=False)

con.commit()
con.close()

