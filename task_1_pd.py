# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 16:08:31 2018

@author: hmohan
"""
import mysql.connector
import xlrd
import os
import pandas
from datetime import datetime
from sqlalchemy import create_engine


'''
book = xlrd.open_workbook('/home/hmohan/Desktop/ins1.xlsx')
sheet = book.sheet_by_name('sheet1')
'''
xl= pandas.ExcelFile('/home/hmohan/Desktop/ins1.xlsx')
#xl.sheet_names
fd1 = xl.parse('Sheet1')

#print (fd1.head())

try:
    engine = create_engine("mysql+mysqlconnector://root:admin@localhost/mydb")

    con = engine.connect()
    
except Exception as e:
    print (e)
try:
    fd1.to_sql(name='INS1',con=con,if_exists='append')
    con.close()
    print ('table added')
except Exception as e:
    print(e)


xl= pandas.ExcelFile('/home/hmohan/Desktop/vio1.xlsx')
#xl.sheet_names
fd1 = xl.parse('Sheet1')

#print (fd1.head())

engine = create_engine("mysql+mysqlconnector://root:admin@localhost/mydb")

con = engine.connect()
fd1.to_sql(name='VIO1',con=con,if_exists='append')
print ('table added')














'''
database = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='admin',
                                   database='mydb'
                                   )
cursor = database.cursor()
#cursor.execute("CREATE TABLE VIO (points VARCHAR(255),serial_number VARCHAR(255),violation_code VARCHAR(255),violation_description VARCHAR(255),violation_status VARCHAR(255))")

#query = 'INSERT INTO VIO (points,serial_number,violation_code,violation_description,violation_status) VALUES (%s,%s,%s,%s,%s)'                              
fd1.to_sql(name='VIO1',con= database,if_exists = 'append')
'''


