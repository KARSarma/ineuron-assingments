#!/usr/bin/env python
# coding: utf-8

# In[15]:


import csv
import json

csvfile = open('carbon_nanotubes.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("col1","col2","col3","col4","col5","col6","col7")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')


# In[2]:


ls


# In[17]:


file=open("delimiter.csv","w")
writer = csv.writer(file, delimiter = ",")


# In[18]:


file=open("file.json",'r')


# In[16]:


#file=write("file.json",delimiter=",")


# In[19]:


file.read()


# In[25]:


#bulk insertion
import json
import pymongo
from pymongo import MongoClient 
  
  
# Making Connection
myclient = pymongo.MongoClient("mongodb+srv://KARS:black97tiger19@cluster0.wjf4l.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
   
# database 
db = myclient["GFG"]
   
# Created or Switched to collection 
# names: GeeksForGeeks
Collection = db["data"]
  
# Loading or Opening the json file
#with open('file.json') as file:
file=open('file.json','r')
#data = json.load(file)
data = [json.loads(line) for line in file]
      
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else inser_one is used
if isinstance(data, list):
    Collection.insert_many(data)  
else:
    Collection.insert_one(data)


# In[26]:


#insertion 
dict1 = {
    "col1" :"10;1;0",
    "col2" :"270267;0",
    "col3" :"331105;0",
    "col4" : "879684;0",
    "col5" : "359867;0",
    "col6": "34534534635",
    "col7": "910979"
}


# In[29]:


Collection.insert_one(dict1)


# In[32]:


#update many
Collection.update_many({'col1': '10;6;0'},{"$set":{'col1': '10;4;0'}})


# In[33]:


#update one
Collection.update_one({'col6': '34534534635'},{"$set":{'col6': '4534534635'}})


# In[36]:


#deletion many
Collection.delete_many({'col6': '4534534635'})


# In[37]:


#deletion one
Collection.delete_one({'col1': '10;6;0'})


# In[38]:


#find operations

for i in Collection.find():
    print(i)


# In[39]:


#find one
oll.find_one()


# In[ ]:




