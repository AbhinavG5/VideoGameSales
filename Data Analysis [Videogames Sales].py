#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries & Database

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import os


# In[3]:


# DATABASE
df = pd.read_csv('vgsales.csv')


# In[49]:


# ROWS AND COLUMNS
df.shape


# In[50]:


# FIRST 5 ROWS
df.head()


# # Data Cleaning

# In[8]:


# SUMMARY OF DATASET
df.info()


# In[9]:


# CHECKING MISSING COLUMNS
pd.isnull(df).sum()


# In[10]:


df.dropna(inplace = True)


# In[12]:


# AFTER CLEANING THE MISSING COLUMNS
pd.isnull(df).sum()


# In[16]:


# COLUMN NAMES
df.columns


# In[14]:


# SUMMARY OF DESCRIPTIVE STATISTICS OF DATASET
df.describe()


# # Exploratory Data Analysis and Visualisation

# In[51]:


# COLUMN NAMES
df.columns


# ### North America Sales by Genre

# In[60]:


# GRAPH PLOTING

plt.figure(figsize =(12,8))
sales_gen = df.groupby(['Genre'], as_index=False)['NA_Sales'].sum()
plt.title('North America Game Sales by Genre' , fontsize =15)
sns.barplot(x = 'Genre', y = 'NA_Sales', data = sales_gen,)


# ### Global Sales by Genre

# In[59]:


# GRAPH PLOTING

plt.figure(figsize =(12,8))
sales_gen = df.groupby(['Genre'], as_index=False)['Global_Sales'].sum()
plt.title('Global Game Sales by Genre' , fontsize =15)
sns.barplot(x = 'Genre', y = 'Global_Sales', data = sales_gen)


# ### Japan Sales by Genre

# In[58]:


# GRAPH PLOTING

plt.figure(figsize =(12,8))
sales_gen = df.groupby(['Genre'], as_index=False)['JP_Sales'].sum()
plt.title('Japan Game Sales by Genre' , fontsize =15)
sns.barplot(x = 'Genre', y = 'JP_Sales', data = sales_gen)


# ### Top 20 Most Sold Games of all Time

# In[18]:


# MOST SOLD GAMES
df.head(20)


# In[74]:


# PIECHART

x=[82.74, 40.24, 35.82, 33, 31.37, 30.26, 30.01, 29.02, 28.62, 28.31, 24.76, 23.42, 23.10, 22.72, 22, 21.82, 21.40, 20.81, 20.61, 20.22]
fig = plt.figure(figsize =(6.6, 6.6))

plt.pie(x, labels=("Wii Sports", "Super Mario Bros","Mario Kart Wii","Wii Sports Resort", "Pokemon Red/Pokemon Blue", "Tetris", "Super Mario Bros","New Super Mario Bros","Wii Play", "New Super Mario Bros. Wii", "Duck Hunt", "Nintendogs", "Mario Kart DS", "Pokemon Gold/Pokemon Silver", "Wii Fit", "Wii Fit Plus", "Kinect Adventures!", "Grand Theft Auto V", "Grand Theft Auto: San Andreas", "Super Mario World"))
plt.title('Most Sold Videogames of all Time', fontsize = 20)
plt.xlabel('"Based on Global Sales of Each Game"', fontsize = 8)
plt.pie(x)
plt.show()


# In[ ]:




