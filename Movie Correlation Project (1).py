#!/usr/bin/env python
# coding: utf-8

# In[108]:


# import libraries
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None

#read in the data
df=pd.read_csv('movies[1].csv')


# In[109]:


#let's look at the data 
print(df)


# In[110]:


df.head()


# In[111]:


df.tail()


# In[112]:


df=df.dropna()


# In[113]:


print(df)


# In[114]:


df.tail()


# In[115]:


#lets see if there is any missing data
for col in df.columns:
    pct_missing=np.mean(df[col].isnull())
    print('{}-{}%'.format(col,round(pct_missing*100)))


# In[117]:


df['budget']= df['budget'].astype('int64')
df['gross']= df['gross'].astype('int64')


# In[153]:


df.head()


# In[119]:


df=df.sort_values(by=['gross'],inplace=False,ascending=False)


# In[120]:


pd.set_option('display.max_rows',None)


# In[121]:


# drop any duplicates
df.drop_duplicates()


# In[84]:


# budget gonna have high correlation gross revenue
#company having high correlation with the gross revenue


# In[154]:


df['Year'] = df['released'].astype(str)
df.head()


# In[90]:


#scatter plot with budget vs gross revenue

plt.scatter(x=df['budget'],y=df['gross'],alpha=0.5)

plt.title('Budget vs Gross Earnings')
plt.show()


# In[57]:


df.head()


# In[63]:


#plot budget vs gross using seaborn to know the coreelation b/w two

sns.regplot(x='budget',y='gross',data=df,scatter_kws={"color":"red"}, line_kws={"color":"blue"})


# In[67]:


#lets start looking at correlation
df.corr(method='pearson')


# In[68]:


#result = high correlation between budget vs gross


# In[92]:


correlation_matrix=df.corr(method='pearson')
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix for Numeric Features')
plt.show()


# In[135]:


#looks at company



# In[155]:


df_numerized= df
for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name]= df_numerized[col_name].astype('category')
        df_numerized[col_name]= df_numerized[col_name].cat.codes
                                  
df_numerized.head()


# In[156]:


df.head()


# In[136]:


correlation_matrix=df_numerized.corr(method='pearson')
sns.heatmap(correlation_matrix, annot=True)
plt.title('Correlation Matrix for Numeric Features')
plt.show()


# In[138]:


df_numerized.corr()


# In[143]:


correlation_mat = df_numerized.corr()
corr_pairs=correlation_mat.unstack()
corr_pairs


# In[144]:


sorted_pairs = corr_pairs.sort_values()
sorted_pairs


# In[152]:


high_correlation = sorted_pairs[(sorted_pairs)>0.5]
high_correlation


# In[ ]:


#votes and budget has high correlation towards gross earnings
# budget and company has low correlation 

