#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd #handling the data


# In[8]:


import matplotlib.pyplot as plt #visualisation of scatterplot


# In[9]:


from scipy.stats import pearsonr #to check strength of the correlation (r value)


# In[10]:


df=pd.read_csv('Auto.csv')


# In[11]:


df.head()


# In[12]:


df.tail()


# In[14]:


x=df['weight']# to determine the x and Y 
y=df['mpg']


# In[22]:


plt.scatter(x,y)
plt.show()


# In[29]:


plt.scatter(x,y)
plt.title('Automobile Analysis')
plt.xlabel('weight')
plt.ylabel('mpg')
plt.show()


# In[28]:


df.corr()


# In[15]:


#-0.8 is r value or co-efficient correlation value.The value denotes the strength of the correlation between two variables


# In[ ]:


negative correlation.

