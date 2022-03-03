#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[2]:


import mysql.connector as conn


# In[3]:


conn.connect(host = 'localhost',user = 'root' ,passwd = "black97tiger19")


# In[4]:


mydb = conn.connect(host = 'localhost',user = 'root' ,passwd = "black97tiger19")


# In[9]:


cursor = mydb.cursor()


# In[5]:


import pandas as pd


# In[6]:


pd.read_sql("select * from SqlAssignment.worker",mydb)


# In[14]:


#1
cursor.execute("select firstname as worker_name from sqlassignment.worker ")


# In[15]:


cursor.fetchall()


# In[16]:


#2
cursor.execute("select distinct department from sqlassignment.worker ")


# In[17]:


cursor.fetchall()


# In[22]:


#3
cursor.execute("select * from sqlassignment.worker order by emplyeeid desc limit 5 ")


# In[23]:


cursor.fetchall()


# In[ ]:




