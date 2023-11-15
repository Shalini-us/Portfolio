#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('diabetes.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.isna().sum()


# In[6]:


df.describe()


# In[7]:


df.info


# In[8]:


df.columns


# In[9]:


Features=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']


# In[13]:


x=df[Features]
y=df.label


# In[14]:


x


# In[15]:


y


# In[16]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train ,y_test=train_test_split(x,y,test_size=0.25,random_state=0)


# In[17]:


x_test


# In[18]:


x_train


# In[19]:


y_train


# In[20]:


y_test


# In[23]:


from sklearn.ensemble import GradientBoostingClassifier


# In[24]:


gb_class=GradientBoostingClassifier(n_estimators=90,random_state=0)


# In[25]:


gb_class.fit(x_train,y_train)


# In[27]:


y_pred=gb_class.predict(x_test)


# In[28]:


y_pred


# In[29]:


y_test


# In[34]:


import matplotlib.pyplot as plt
from sklearn import metrics

confusion_matrix= metrics.confusion_matrix(y_test,y_pred)
confusion_matrix= metrics.ConfusionMatrixDisplay(confusion_matrix,display_labels=[True,False])
confusion_matrix.plot()
plt.show()


# In[36]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)


# In[42]:


from sklearn.metrics import precision_score
precision_score (y_test,y_pred)*100


# In[43]:


from sklearn.metrics import recall_score
recall_score (y_test,y_pred)*100


# In[41]:


F1_score = metrics.f1_score(y_test,y_pred)
print(F1_score)


# In[ ]:




