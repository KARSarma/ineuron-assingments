#!/usr/bin/env python
# coding: utf-8

# In[10]:


import mysql.connector as conn


# In[11]:


conn.connect(host = 'localhost',user = 'root' ,passwd = "black97tiger19")


# In[12]:


mydb = conn.connect(host = 'localhost',user = 'root' ,passwd = "black97tiger19")


# In[13]:


cursor = mydb.cursor()


# In[14]:


import pandas as pd


# In[15]:


pd.read_sql("select * from SqlAssignment.worker",mydb)


# In[30]:


#1
cursor.execute("select salary from SqlAssignment.worker ORDER BY `salary` ASC limit 4,1")


# In[31]:


cursor.fetchall()


# In[32]:


#2
cursor.execute("select * from sqlassignment.worker where salary in(select salary from sqlassignment.worker GROUP BY salary HAVING COUNT(1)>1)order by salary desc")


# In[33]:


cursor.fetchall()


# In[ ]:




