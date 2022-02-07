#!/usr/bin/env python
# coding: utf-8

# In[15]:


#1
a=[]
b=int(input("enter the size of array: "))
print("enter array numbers: ")
for i in range(b):
    num=int(input())
    a.append(num)
print("sum of array",sum(a))


# In[14]:


#2
a=[]
l=int(input("enter the size of array: "))
print("enter array numbers: ")
for i in range(l):
    num=int(input())
    a.append(num)
print("largest element in array",max(a))


# In[19]:


#3
def rotateArray(a,d):
    temp = []
    n=len(a)
    for i in range(d,n):
        temp.append(a[i])
    i = 0
    for i in range (0,d):
        temp.append(a[i])
    a=temp.copy()
    return a
 
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, 2))


# In[22]:


#4
def SplitArray(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]

    arr[n-1] = x
arr = [15, 40, 15, 16, 50, 36]
n = len(arr)
position = 2
SplitArray(arr, n, position)
for i in range(0, n):
    print(arr[i], end = ' ')


# In[23]:


#5
def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
  

A = [6, 5, 4, 4]
  

print(isMonotonic(A))


# In[ ]:




