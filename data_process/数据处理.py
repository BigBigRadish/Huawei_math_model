# -*- coding: utf-8 -*-
'''
Created on 2018��9��15��

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
import pandas as pd 
# xlsx=pd.read_excel('../InputData.xlsx',sheetname='Gates')
# print(xlsx)
# xlsx.to_csv('../Gates.csv')
pucks=pd.read_csv('../dataset/pucks.csv',skiprows=0)
list_w=['332','333','33E','33H','33L','773']
list_n=['319','320','321','323','325','738','73A','73E','73H','73L']
air_type=[]
#print(pucks['飞机型号'])
for i in pucks['飞机型号']:
    if str(i)in list_n:
        air_type.append('W')
    else:
        air_type.append('N')
# print(len(air_type),air_type)
pucks['机体类别']=air_type
pucks.to_csv('../dataset/pucks_1.csv')
        
