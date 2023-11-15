#!/usr/bin/env python
# coding: utf-8
import pandas as pd
# In[66]:


data=pd.read_csv('HeartDisease.csv')


# In[67]:


data.head()


# In[68]:


data.tail()


# In[69]:


data.columns


# In[70]:


features=['age', 'gender', 'chest_pain', 'rest_bps', 'cholestrol',
       'fasting_blood_sugar', 'rest_ecg', 'thalach', 'exer_angina', 'old_peak',
       'slope', 'ca', 'thalassemia',]


# In[71]:


x=data[features]


# In[72]:


y=data.target


# In[73]:


x


# In[74]:


y


# In[118]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=0)


# In[119]:


x_test


# In[120]:


x_train


# In[121]:


y_test


# In[122]:


y_train


# In[123]:


from sklearn.tree import DecisionTreeClassifier


# In[124]:


dt=DecisionTreeClassifier()


# In[125]:


dt.fit(x_train, y_train)


# In[128]:


y_pred=dt.predict(x_test)


# In[129]:


y_pred


# In[130]:


y_test


# In[138]:


import matplotlib.pyplot as plt
from sklearn import metrics

confusion_matrix = metrics.confusion_matrix(y_test,y_pred)
confusion_matrix = metrics.ConfusionMatrixDisplay(confusion_matrix,display_labels=[False,True])
confusion_matrix.plot()
plt.show()


# In[139]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)


# In[140]:


from sklearn.metrics import precision_score
precision_score(y_test,y_pred,average=None)


# In[141]:


from sklearn.metrics import recall_score
recall_score(y_test,y_pred,average=None)*100


# In[142]:


F1_score=metrics.f1_score(y_test,y_pred)
print(F1_score)


# In[ ]:




