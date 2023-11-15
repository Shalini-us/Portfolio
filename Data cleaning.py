#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #for manipulating data,pd is not mandatory anyname can be set according to that makes changes in next execution.


# In[4]:


df=pd.read_csv('dirtydata.csv') #df also not constant can be write any name.


# In[5]:


print(df) #to get the data from the system


# In[47]:


df.head() #ensuring data has been properly uploaded or not its a first 5 rows and colums present


# In[8]:


df.tail() #last 5 rows, if you want more rows last 10 then in a brackets type 10


# # Removing empty cells

# In[10]:


#method 1
new_df=df.dropna() #removing empty cells


# In[11]:


print(new_df)


# In[20]:


#method 2
df.fillna(777,inplace=True) #replacing the empty cells by some numbers


# In[14]:


print(df)


# In[21]:


#method 3
import pandas as pd
df=pd.read_csv('dirtydata.csv')
df['Calories'].fillna(250,inplace=True) #replacing the empty cells by 250 in specific columns


# In[17]:


print(df)


# # wrong format

# In[22]:


df=pd.read_csv('dirtydata.csv')


# In[ ]:


df['Date']=pd.to_datetime(df['Date'])


# In[30]:


print(df)


# # wrong data

# In[25]:


df=pd.read_csv('dirtydata.csv')


# In[31]:


df.loc[7,'Duration']=50 #replacing the abnormal data in row 7 as normal


# In[32]:


print (df)


# # duplicates

# In[40]:


df=pd.read_csv('dirtydata.csv')


# In[43]:


df.drop_duplicates(inplace=True)#removing duplicates


# In[44]:


print(df)


# In[45]:


df.isna().sum()# how many empty cell present in the data


# In[46]:


df.info()# how many empty cell present in the data and also present data types(integer,floar,string)


# In[ ]:




