#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[66]:


filename = 'data2.csv'
df = pd.read_csv(filename, encoding='Windows-1251', header = None)
df = df.rename(columns={0:'Навык', 1:'Вакансии',2:'Соискатели'})


# In[54]:


df['Человек на вакансию'] = (df['Соискатели'] / df['Вакансии']).round(0)
df1 = df.sort_values('Вакансии', ascending = False)


# In[55]:


sns.set(
    font_scale=2,
    style="whitegrid",
    rc={'figure.figsize':(20,7)}
    )


# In[56]:


ax = sns.barplot(data = df1, y='Вакансии', x='Навык') 
plt.xticks(rotation=90)

plt.show()


# In[57]:


bx = sns.barplot(data = df1, y='Человек на вакансию', x='Навык') 
plt.xticks(rotation=90)

plt.show()


# In[62]:


cx = sns.lineplot(data = df1, x='Навык', y='Соискатели')
cx = sns.lineplot(data = df1, x='Навык', y='Вакансии')
plt.xticks(rotation=90)

plt.show()


# In[69]:


df.dtypes


# In[70]:


df.columns


# In[72]:


df.describe()


# In[ ]:




