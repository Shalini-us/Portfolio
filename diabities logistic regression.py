#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd


# In[18]:


df=pd.read_csv('diabetes.csv')


# In[19]:


df.head()


# In[20]:


df.tail()


# In[21]:


df.info()


# In[22]:


df.isnull().sum() #method1:df.isna


# In[26]:


df.columns


# In[27]:


features=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']


# In[29]:


x=df[features]


# In[31]:


y=df.label


# In[32]:


x


# In[33]:


y


# In[36]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=25)


# In[37]:


x_train


# In[38]:


x_test


# In[39]:


y_test


# In[40]:


y_train


# In[66]:


from sklearn.linear_model import LogisticRegression


# In[67]:


logreg=LogisticRegression()


# In[70]:


logreg.fit(x_train,y_train)


# In[71]:


y_pred=logreg.predict(x_test)


# In[72]:


y_pred


# In[73]:


y_test


# In[75]:


#evaluating the metrics #performance of the model


# In[84]:


import matplotlib.pyplot as plt
from sklearn import metrics

confusion_matrix =metrics.confusion_matrix(y_test,y_pred)
confusion_matrix =metrics.ConfusionMatrixDisplay(confusion_matrix,display_labels=[False,True])
confusion_matrix.plot()
plt.show()


# In[85]:


# accuracy


# In[86]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)


# In[89]:


#precision
from sklearn.metrics import precision_score
precision_score(y_test,y_pred,average=None)


# In[90]:


# 81% got model predicted true negative,69% predicted true positive values 


# In[92]:


#recall (proportions with false positive and false negative)
from sklearn.metrics import recall_score
recall_score(y_test,y_pred,average=None)*100 


# In[93]:


F1_score=metrics.f1_score(y_test,y_pred)
print(F1_score)


# In[ ]:




