#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyodbc


# In[ ]:


class N41DB:
    def __init__(self, username ='', password ='', server = ''):
        self.username = username
        self.password = password
        self.server = server
        self.conn = None
        self.cursor = None
    #db.key
    def loadKey(self, path):
        with open(path, 'r') as f:
            self.username = f.readline().strip()
            self.password = f.readline().strip()
            self.server = f.readline().strip()
        return
    
    def connectDB(self,database):
        self.conn = pyodbc.connect('Trusted_Connection=yes;'+'DRIVER={SQL Server Native Client 11.0};SERVER='+self.server+';DATABASE='+database+';UID='+self.username+';PWD='+ self.password+';Encrypt=no;autocommit=True')
        self.cursor = self.conn.cursor()
    def dropDB(self):
        self.cursor.close()
        self.conn.close()

