# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 17:18:44 2018

@author: hmohan
"""

import mysql.connector
import xlrd
import os
import pandas
from datetime import datetime
from sqlalchemy import create_engine



try: 
    xl= pandas.ExcelFile('/home/hmohan/Desktop/inspections .xlsx')
#xl.sheet_names
    fd1 = xl.parse('inspections')

#print (fd1.head())

    engine = create_engine("mysql+mysqlconnector://root:admin@localhost/mydb")

    con = engine.connect()
    fd1.to_sql(name='INSPECTIONS',con=con,if_exists='append')
    con.close()
    print ('table apdded')
except Exception:
    print (e)


xl= pandas.ExcelFile('/home/hmohan/Desktop/violations.xlsx')
#xl.sheet_names
fd1 = xl.parse('violations')

#print (fd1.head())

engine = create_engine("mysql+mysqlconnector://root:admin@localhost/mydb")

con = engine.connect()
fd1.to_sql(name='VIOLATIONS',con=con,if_exists='append')
con.close()
print ('table added')