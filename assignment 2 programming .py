#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Assignment 2 programming 


# In[7]:


#question 1

print("enter kilometers")
a=float(input())

print("entered kilometers in miles is")
b=a*0.621371
print(b)


# In[13]:


#question 2

celsius = float (input("Celsius: " ))  
Fahrenheit = (celsius * 9/5) + 32  
    

print ('The %.2f Celsius is equal to: %.2f Fahrenheit'  
      %(celsius, Fahrenheit))  


# In[20]:


#question 3

#printin calendar of january 2022
import calendar 

yy=2022
mm=1

print(calendar.month(yy,mm))


# In[28]:


#question 4

import cmath

a = int(input())
b = int(input())
c = int(input())

#discriminant
d = (b**2) - (4*a*c)

#solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print(sol1,sol2)


# In[29]:


#question 5

a = input()
b = input()
 
print("Before a : ", a, " and b : ", b)
 
a, b = b, a
 

print("after a : ", a, " and b : ", b)


# In[ ]:




