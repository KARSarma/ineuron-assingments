#!/usr/bin/env python
# coding: utf-8

# In[7]:


#1
import math
def check(n) :
    count_digits = len(str(n))
   
    sum = 0 
    x = n
    while (x!=0) :
 
        r = x % 10
        sum = (int) (sum + math.pow(r, count_digits))
        count_digits = count_digits - 1
        x = x//10
        
    if sum == n :
        return 1
    else :
        return 0
       
n = int(input("enter the number: "))
if (check(n) == 1) :
    print ("Disarium Number",n)
else :
    print ("Not a Disarium Number")


# In[36]:


#2
def Length(n):    
    length = 0;    
    while(n != 0):                   
        length = length + 1;    
        n = n//10;    
    return length;    
     
def sumdigit(num):    
    rem = sum = 0;    
    len = Length(num);    
        
    while(num > 0):    
        rem = num%10;   
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
      
result = 0;    
     

print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):        
    result = sumdigit(i);    
        
    if(result == i):    
        print(i),   


# In[38]:


#3
def isHappy(n):    
    r = s = 0;    
    while(n > 0):    
        r = n%10    
        s += r**2  
        n //= 10    
    return s  
        
n = int(input())    
res = n;    
     
while(res != 1 and res != 4):    
    res = isHappy(res)    
     
if(res == 1):    
    print("happy number");    
elif(res == 4):    
    print("not a happy number");   


# In[42]:


#4
def isHappyNumber(num):
    rem = sum = 0
      
    while(num > 0):
        rem = num%10
        sum = sum + (rem*rem)
        num = num//10;
    return sum;

print("List of happy numbers between 1 and 100: ")
for i in range(1, 101):
    result = i;
      
    while(result != 1 and result != 4):
        result = isHappyNumber(result)
    if(result == 1):
        print(i)


# In[46]:


#5
a = int(input("enter a number: "))    
rem = sum = 0   
     
n = a    
     
while(a > 0):    
    rem = a%10   
    sum = sum + rem;   
    a = a//10    
         
if(n%sum == 0):    
    print(str(n) + " is a harshad number")    
else:    
    print(str(n) + " is not a harshad number")


# In[49]:


#6 
def PronicNumber(num):    
    flag = False   
        
    for j in range(1, num+1):      
        if((j*(j+1)) == num):    
            flag = True   
            break    
    return flag    
         
print("Pronic numbers between 1 and 100: ")    
for i in range(1, 101):    
    if(PronicNumber(i)):    
        print(i)  


# In[ ]:




