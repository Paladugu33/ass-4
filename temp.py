# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:48:04 2018

@author: hmohan
"""

import pandas as pd
#import xlrd

xl= pd.ExcelFile('/home/hmohan/Desktop/ins1.xlsx')
#xl.sheet_names
fd1 = xl.parse('Sheet1')

xl= pd.ExcelFile('/home/hmohan/Desktop/vio1.xlsx')
fd2 = xl.parse('Sheet1')

fd=pd.merge(fd2,fd1,on=['serial_number'])

df = pd.DataFrame()
df = fd[['activity_date','violation_code']].copy()


df['activity_date'].to_datetime()


'''
#df=pd.DataFrame(df.groupby('activity_date')['activity_date'].count())
#print (df['activity_date'])
#print (type(df['activity_date']))

#df.columns=['count']
#print (df['count'])
#print(df['2015/12/01'].value_counts())
'''