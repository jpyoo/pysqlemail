#!/usr/bin/env python
# coding: utf-8

# In[1]:


from modules.renew_report import renewData
from modules.Email_Report import sendMail


# In[ ]:


renewData()

sendMail('email_data.json')

