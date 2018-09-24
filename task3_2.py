# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 11:37:46 2018

@author: hmohan
"""


import xlsxwriter
import mysql
import pandas as pd


workbook=xlsxwriter.Workbook("Violationstype.xlsx")
worksheet = workbook.add_worksheet("violations type")

df=pd.read_excel('Violationstype.xlsx')

tot=(df.sum()['count'])
#row= len(myresult)
worksheet.write(118,1,'total count:')
worksheet.write(118,2,tot)

workbook.close()