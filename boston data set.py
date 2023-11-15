#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv('Boston.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# # Determine Feature & Label (x&y)¶

# In[10]:


#method 1


# In[14]:


x=df.iloc[:,1:14]
y=df['medv']


# In[15]:


x


# # method 1:

# In[16]:


y


# In[17]:


df_new=df.drop('medv',axis=1)
df_new.head()


# # method 2:

# In[18]:


y


# In[20]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.20,random_state=0)


# In[21]:


x_train


# In[22]:


x_test


# In[23]:


y_test


# In[24]:


y_train


# In[25]:


#train the algorithm


# In[26]:


from sklearn.linear_model import LinearRegression


# In[27]:


regressor=LinearRegression()


# In[28]:


regressor.fit(x_train,y_train)


# In[29]:


y_pred=regressor.predict(x_test)


# In[30]:


y_pred


# In[31]:


y_test


# In[43]:


from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score


# In[45]:


print('MAE', mean_absolute_error(y_test, y_pred))


# In[33]:


r2=r2_score(y_test,y_pred)


# In[46]:


print('MSE',mean_absolute_error (y_test, y_pred))


# In[34]:


print(r2) #r2 values should be high Rmse should be minimum


# In[47]:


from math import sqrt
print ('RMSE',sqrt(mean_absolute_error(y_test, y_pred)))


# In[ ]:


#r2 is low hence it is not a good model

