#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Assignment 1 programming 


# In[7]:


#question 1
print("Hello Python")


# In[10]:


#question 2
a=10 
b=20
c=a+b
print(c)
d=a/b
print(d)


# In[17]:


#question 3
#enter 3 sides of triangle
a=float(input())
b=float(input())
c=float(input())

#calculating semi-perimeter
s=( a+ b +c)/2

#calculating area
area= (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)


# In[20]:


#question 4
a=input()
b=input()
temp=a
a=b
b=temp
print("this is a",a,"this is b", b)


# In[23]:


#question 5

import random
print(random.randint(0,9))


# In[ ]:




