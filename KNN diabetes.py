#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd
import seaborn as sn


# In[64]:


df=pd.read_csv('diabetes.csv')


# In[65]:


df.head()


# In[66]:


df.tail()


# In[67]:


df.isnull().sum()


# In[68]:


df.info()


# In[69]:


df.hist(figsize=(10,10))


# In[ ]:


sn.pairplot(df)


# In[71]:


sn.heatmap(df.corr(),annot=True)


# In[72]:


#determining the x and y


# In[73]:


df.columns


# In[74]:


features=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']


# In[75]:


x=df[features]
y=df.label


# In[76]:


x


# In[36]:


y


# In[37]:


#split the data set into training the test


# In[ ]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)


# In[ ]:


x_train


# In[40]:


y_train


# In[41]:


x_test


# In[42]:


y_test


# In[43]:


#train the algoritm


# In[44]:


from sklearn.neighbors import KNeighborsClassifier


# In[45]:


knn=KNeighborsClassifier(n_neighbors=3)


# In[46]:


knn.fit(x_train,y_train)


# In[47]:


#prediticting the x test data


# In[48]:


y_pred=knn.predict(x_test)


# In[49]:


y_pred #model predicted


# In[50]:


y_test #actual output for your X_test


# In[51]:


#evaluating the performance of the model


# In[52]:


import matplotlib.pyplot as plt
from sklearn import metrics  

confusion_matrix=metrics.confusion_matrix(y_test,y_pred)
confusion_matrix=metrics.ConfusionMatrixDisplay(confusion_matrix,display_labels=[True,False])
confusion_matrix.plot()
plt.show()


# In[53]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)


# In[54]:


from sklearn.metrics import precision_score
precision_score(y_test,y_pred,average=None)


# In[55]:


from sklearn.metrics import recall_score
recall_score(y_test,y_pred,average=None)


# In[56]:


F1_score=metrics.f1_score(y_test,y_pred)
print (F1_score)


# In[ ]:




