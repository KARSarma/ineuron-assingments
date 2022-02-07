#!/usr/bin/env python
# coding: utf-8

# In[8]:


#1


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
mat = [[int(input()) for x in range (C)] for y in range(R)]

result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)


# In[7]:


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
mat = [[int(input()) for x in range (C)] for y in range(R)]
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
    print(r)


# In[9]:


#3
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  
mat = [[int(input()) for x in range (C)] for y in range(R)]

result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for r in result:
   print(r)


# In[11]:


#4


my_str = str(input())

words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are:")
for word in words:
   print(word)


# In[14]:


#5
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = str(input())

no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

print(no_punct)


# In[ ]:





# In[ ]:




