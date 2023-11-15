#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


from scipy.stats import pearsonr


# In[4]:


df=pd.read_excel('BPO.xlsx')


# In[5]:


df.head()


# In[8]:


df.tail()


# In[9]:


x=df['Cyclce_time']
y=df['Hold_time']


# In[10]:


plt.scatter(x,y)
plt.show()


# In[11]:


plt.scatter(x,y)
plt.title('BPO Analysis')
plt.xlabel('Cyclce_time')
plt.ylabel('Hold_time')
plt.show()


# In[25]:


df.corr()


# In[ ]:


# conclusion:when cycle time increases hold time also increases.


# In[ ]:




