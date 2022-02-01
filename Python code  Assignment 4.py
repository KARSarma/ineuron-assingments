#!/usr/bin/env python
# coding: utf-8

# In[10]:


#1
a=int(input())
factorial=1
if a<0 or a==0:
    print("1 is the factorial")
else:
    for i in range(1,a+1):
        factorial= factorial*i
    print("The factorial of",a,"is",factorial)
        
   


# In[21]:


#2
a=int(input("multiplicaion table of "))

for i in range(1, 11):
    print(a, 'x', i, '=', a*i)


# In[25]:


#3


a= int(input("How many terms? "))

n1, n2 = 0, 1
count = 0
if a <= 0:
   print("enter a positive integer")
elif a== 1:
   print("Fibonacci sequence upto",a,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < a:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


# In[42]:


#4
a = int(input("Enter a number: "))

sum = 0
t = a
while t > 0:
    digit = t % 10
    sum +=digit ** 3
    t //= 10
if a == sum:
       print(a,"is an Armstrong")
else:
       print(a,"is not an Armstrong")


# In[48]:


#5
# Program to check Armstrong numbers in a certain interval

lower = int(input("lower: "))
upper = int(input("upper: "))

for a in range(lower, upper + 1):
    order = len(str(a))
    sum = 0
    t = a
    while t > 0:
        digit = t % 10
        sum += digit ** order
        t //= 10

    if a == sum:
        print(a)


# In[64]:


#6

a=int(input("enter the number: "))
if a<0:
    print("enter a positive number")
else:
    sum = (a*(a+1)/2)
print("sum of number till",a,"is",sum)


# In[ ]:




