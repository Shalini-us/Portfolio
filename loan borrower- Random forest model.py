#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


loan=pd.read_csv('loan_borowwer_data.csv')


# In[5]:


loan.head()


# In[6]:


loan.tail()


# In[9]:


loan.isnull().sum()


# In[11]:


loan.describe()


# In[13]:


loan.info()


# # setting up the data

# In[1]:


gd=['purpose']


# In[24]:


final_data=pd.get_dummies(loan,columns=gd,drop_first=True)


# In[25]:


final_data.info()


# In[27]:


final_data.head()


# In[28]:


#determining x and y


# In[32]:


x=final_data.drop('not.fully.paid',axis=1)
y=final_data['not.fully.paid']


# In[33]:


x


# In[34]:


y


# In[35]:


#SPLITTING THE DATA SET INTO TRAINING $ TESTING


# In[38]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)


# In[39]:


x_train


# In[40]:


y_train


# In[41]:


y_test


# In[42]:


x_test


# In[57]:


from sklearn.tree import DecisionTreeClassifier #train the algorithm


# In[52]:


dt= DecisionTreeClassifier()


# In[53]:


dt.fit(x_train, y_train)


# In[54]:


y_pred=dt.predict(x_test) #predicting the test data set x_test


# In[55]:


y_pred


# In[56]:


y_test


# In[95]:


from sklearn.ensemble import RandomForestClassifier


# In[96]:


rfc= RandomForestClassifier (n_estimators=600) #number of trees


# In[99]:


rfc.fit(x_train, y_train)


# In[102]:


y_pred=rfc.predict(x_test)


# In[103]:


y_pred


# In[105]:


y_test #actual


# In[107]:


import matplotlib.pyplot as plt
from sklearn import metrics

confusion_matrix =metrics.confusion_matrix(y_test,y_pred)
confusion_matrix= metrics.ConfusionMatrixDisplay(confusion_matrix,display_labels=[False,True])
confusion_matrix.plot()
plt.show()


# In[108]:


#accuracy


# In[109]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)


# In[111]:


from sklearn.metrics import precision_score
precision_score(y_test,y_pred, average=None)


# In[112]:


#recall


# In[113]:


from sklearn.metrics import recall_score
recall_score(y_test,y_pred,average=None)


# In[115]:


F1_score=metrics.f1_score(y_test, y_pred)
print(F1_score)


# In[ ]:




