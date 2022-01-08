#!/usr/bin/env python
# coding: utf-8

# In[1]:


from modules.DBsql import N41DB
import pandas as pd


# In[7]:


def renewData():
    n41db  = N41DB()
    n41db.loadKey(r'C:\emailreport\db.key')

    n41db.connectDB('N41') # your database name goes here

    sql_query = pd.read_sql_query('''
                                --Your Query Goes Here
                                  '''
                                  ,n41db.conn)
    df = pd.DataFrame(sql_query)
    df.to_csv (r'C:\emailreport\data\Sold Out Wiht OH.csv', index = False) # place 'r' before the path name

