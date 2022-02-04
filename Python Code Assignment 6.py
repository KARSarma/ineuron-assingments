#!/usr/bin/env python
# coding: utf-8

# In[17]:


#1


def re_fibo(n):
    if n <= 1:
        return n
    else:
        return(re_fibo(n-1) + re_fibo(n-2))

a = int(input("enter the lenght: "))

if a <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(a):
        print(re_fibo(i))


# In[29]:


#2
def re_facto(n):
    if (n>=1):
        return n*re_facto(n-1);
    else:
        return 1

a = int(input("enter a number: "))

if a < 0:
    print("Plese enter a positive integer")
elif a == 0:
    print("Factorial is",re_facto(a) )
else:
    print("Factorial are: ",re_facto(a))


# In[34]:


#3
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

print("your BMI is: ",BMI)


# In[35]:


#4
import math

x=float(input("enter a positive number: "))
math.log( x )


# In[38]:


#5
def sumOfcubes(n):
    sum = 0
    for i in range(1, n+1):
        sum +=i*i*i
          
    return sum
  
n = int(input("Enter a number: "))
print("sum of cubes is: ",sumOfcubes(n))
  


# In[ ]:




