#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
import statistics as st
import seaborn as sn


# In[12]:


df=pd.read_csv('HeartDisease.csv')


# In[13]:


df.head()


# In[14]:


df.tail()


# In[15]:


df.isna().sum()


# In[16]:


df.describe()


# In[17]:


df.hist(figsize=(10,10))


# In[18]:


sn.pairplot(df)


# In[19]:


sn.heatmap(df.corr(),annot=True)


# In[20]:


#determining x and y


# In[99]:


x=df.drop('target', axis=1)
y=df['target']


# In[100]:


x


# In[101]:


y


# In[102]:


#split the data set into training the test


# In[117]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=0)


# In[118]:


x_train


# In[119]:


y_train


# In[120]:


x_test


# In[121]:


y_test


# In[122]:


#train the algorithm


# In[123]:


from sklearn.tree import DecisionTreeClassifier


# In[124]:


from sklearn.neighbors import KNeighborsClassifier


# In[125]:


from sklearn.linear_model import LogisticRegression


# In[126]:


model1 = DecisionTreeClassifier()
model2 = KNeighborsClassifier()
model3 = LogisticRegression()


# In[127]:


model1.fit(x_train, y_train)

model2.fit(x_train, y_train)

model3.fit(x_train, y_train)


# In[132]:


y_pred1 = model1.predict(x_test)

y_pred2 = model2.predict(x_test)

y_pred3 = model3.predict(x_test)


# In[133]:


y_pred1


# In[134]:


y_pred2


# In[135]:


y_pred3


# In[137]:


y_test


# In[136]:


#final prediction


# In[142]:


final_pred=np.array([]) #python they are the containers which are able to store more than one item at the same time
for i in range(0, len(x_test)):
    final_pred = np.append(final_pred, st.mode([y_pred1[i],y_pred2[i], y_pred3[i]]))
print(final_pred)


# In[143]:


#evaluating performance model


# In[146]:


import matplotlib.pyplot as plt
from sklearn import metrics

confusion_matrix = metrics.confusion_matrix(y_test, final_pred) #based on mode final pred has been taken
confusion_matrix = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels=[False,True])
confusion_matrix.plot()
plt.show


# In[147]:


# accuracy


# In[153]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test, final_pred)*100


# In[154]:


from sklearn.metrics import precision_score
precision_score(y_test, final_pred)*100


# In[151]:


from sklearn.metrics import recall_score
recall_score(y_test, final_pred)


# In[152]:


F1_score=metrics.f1_score(y_test, final_pred)
print(F1_score)


# In[ ]:




