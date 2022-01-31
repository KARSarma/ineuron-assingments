#!/usr/bin/env python
# coding: utf-8

# In[7]:


#1
a=float(input())
if a>0:
     print("positive")
elif a<0:
     print("negative")
else:
    print("Zero")


# In[12]:


#2
a=int(input())
if a%2==0:
    print("even")
else:
    print("odd")


# In[16]:


#3
a=int(input())
if (a%400==0) and (a%100==0):
    print("leap year")
elif (a%4==0) and (a%100!=0):
    print("leap year")
else:
    print("not a leap year")


# In[30]:


#4
a=int(input())
if a>1:
    for i in range(2,a):
        if (a%i)==0:
            print("not prime")
            break
        else:
            print("prime")
            break
    
       


# In[36]:


#5

for a in range (1,1000):  
    if a > 1:  
        for i in range (2, a):  
            if (a % i) == 0:  
                break  
        else:  
            print (a)  
    
    


# In[ ]:




