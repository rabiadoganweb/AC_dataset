#!/usr/bin/env python
# coding: utf-8

# # AC Data Analysis

# ### Reading the data 

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[64]:


df=pd.read_csv("AC_Data.csv")
df


# Rename the data date column

# In[65]:


df.rename(columns={'0': 'Date'}, inplace=True)
df


# In[66]:


df['Date'] =  pd.to_datetime(df['Date'])


# ### Finding the null value 

# In[67]:


df.isnull().sum()


# ## I will not delete the null values , as i saw some of ACs have null values and some of them have not. To see the power consumption i need the the total of the power. That is the reason I did not remove null values
# 

# Making new Column

# In[69]:


df['date'] = df['Date'].dt.date
df['time'] = df['Date'].dt.time
df['month'] = df['Date'].dt.month_name(locale = 'English')
df['weekday']=df['Date'].dt.week
df["hour"] = df['Date'].dt.hour
df.head(10)


# In[ ]:





# In[79]:


df.describe()


# # The trends of the Ac

# In[80]:


df_new.hist(bins=50, figsize =(20,15))
plt.savefig('Rabıa')
plt.show()


# ### The correlation of Data 

# In[78]:


df.corr()


# TO understand the correlation we need to visualize

# In[77]:


sns.pairplot(df)


# In[76]:


corre_map=df.corr()
top_corre_features = corre_map.index
plt.figure(figsize=(20,20))
df_heatmap = sns.heatmap(df[top_corre_features].corr(), annot = True, cmap='PiYG')


# In[89]:


df_new=df.iloc[:,1:19]
sum_df=df_new.sum()
sum_df


# # The most usage 

# In[97]:


sum_df.max()


# ### AC 18 has the most usage 

# In[101]:


sum_df.min()


# ### AC 10 has the least usage 

# In[100]:


sns.lineplot(data=df, x="hour", y="AC 1")


# In[32]:


sns.lineplot(data=df, x="hour", y="AC 2")


# In[33]:


sns.lineplot(data=df, x="hour", y="AC 3")


# In[34]:


sns.lineplot(data=df, x="hour", y="AC 4")


# In[35]:


sns.lineplot(data=df, x="hour", y="AC 5")


# In[36]:


sns.lineplot(data=df, x="hour", y="AC 6")


# In[37]:


sns.lineplot(data=df, x="hour", y="AC 7")


# In[38]:


sns.lineplot(data=df, x="hour", y="AC 8")


# In[39]:


sns.lineplot(data=df, x="hour", y="AC 9")


# In[40]:


sns.lineplot(data=df, x="hour", y="AC 10")


# In[41]:


sns.lineplot(data=df, x="hour", y="AC 11")


# In[42]:


sns.lineplot(data=df, x="hour", y="AC 12")


# In[ ]:


sns.lineplot(data=df, x="hour", y="AC 13")


# In[43]:


sns.lineplot(data=df, x="hour", y="AC 14")


# In[44]:


sns.lineplot(data=df, x="hour", y="AC 15")


# In[45]:


sns.lineplot(data=df, x="hour", y="AC 16")


# In[46]:


sns.lineplot(data=df, x="hour", y="AC 17")


# In[47]:


sns.lineplot(data=df, x="hour", y="AC 18")

