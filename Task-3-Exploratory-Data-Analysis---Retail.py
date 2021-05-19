#!/usr/bin/env python
# coding: utf-8

# # Task 3 - Exploratory Data Analysis - Business Analytics

# Task: To perform ‘Exploratory Data Analysis’ on the provided dataset ‘SampleSuperstore’
# 
# Libraries/Datasets Used: Pandas, Numpy, MatplotLib, SampleSuperstore.csv

# Task completed during Data Science & Analytics Internship @ The Sparks Foundation

# ### Importing the necessary libraries into the notebook

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Reading and displaying the data from the Dataset

# In[6]:


df = pd.read_csv("C:\\Users\\shubh\\Downloads\\SampleSuperstore.csv")
df.head()


# ### Dropping the unnecessary columns from the data

# In[7]:


df.drop('Country', axis=1, inplace=True)
df.head()


# In[8]:


df.shape


# In[9]:


df.describe()


# In[10]:


df['Quantity'].count()


# ### Distribution Plots

# In[11]:


# Ship Mode
num_bins = 8
plt.hist(df['Ship Mode'], num_bins, facecolor ='blue' , alpha = 0.8)
plt.show()


# In[12]:


# Segment
num_bins = 8
plt.hist(df['Segment'], num_bins, facecolor ='Red' , alpha = 0.9)
plt.show()


# In[13]:


# Postal Code
num_bins = 30
plt.hist(df['Postal Code'], num_bins, facecolor ='orange' , alpha = 0.8)
plt.show()


# In[14]:


# Category
num_bins = 8
plt.hist(df['Category'], num_bins, facecolor ='purple' , alpha = 0.8)
plt.show()


# In[15]:


# Discount
num_bins = 15
plt.hist(df['Discount'], num_bins, facecolor ='green' , alpha = 0.8)
plt.show()


# In[16]:


num_bins = 30
plt.hist(df['Postal Code'], num_bins, facecolor ='blue' , alpha = 0.8)
plt.show()


# ### Sales by Region

# In[18]:


sales_by_region = df.groupby('Region').size()
print(sales_by_region)


# In[19]:


plot_by_region = sales_by_region.plot(title='Sales by Region',xticks=(1,2,3,4))
plot_by_region.set_xlabel('Region')
plot_by_region.set_ylabel('Sales')


# ### Sales by Profit

# In[20]:


sales_by_profit = df.groupby('Profit').size()
print(sales_by_profit)

plot_by_profit = sales_by_profit.plot(title='Sales by Profit', xticks = range(0, 30))
plot_by_profit.set_xlabel('Profit')
plot_by_profit.set_ylabel('Sales')


# ### Sales by Category

# In[21]:


sales_by_category = df.groupby('Category').size()
print(sales_by_category)

plot_by_category = sales_by_category.plot(title='Sales by Category')
plot_by_category.set_xlabel('Category')
plot_by_category.set_ylabel('Sales')


# ### Sales by Ship Mode

# In[23]:


sales_by_shipmode = df.groupby('Ship Mode').size()
print(sales_by_shipmode)

sales_by_shipmode = sales_by_shipmode.plot(title='Sales by Ship Mode')
sales_by_shipmode.set_xlabel('Ship Mode')
sales_by_shipmode.set_ylabel('Sales')


# ### Sales by Segment

# In[24]:


sales_by_segment = df.groupby('Segment').size()
print(sales_by_segment)

sales_by_segment = sales_by_segment.plot(title='Sales by Segment')
sales_by_segment.set_xlabel('Segment')
sales_by_segment.set_ylabel('Sales')


# ### Distribution of Quantity v/s Sales

# In[25]:


# Plotting the distribution of Quantity v/s Sales
df.plot(x='Quantity', y='Sales', style='^')
plt.title('Quantity vs Sales')  
plt.xlabel('Quantity')  
plt.ylabel('Sales')  
plt.show()


# ### Distribution of Discount v/s Sales

# In[26]:


# Plotting the distribution of Discount v/s Sales
df.plot(x='Discount', y='Sales', style='o')
plt.title('Discount vs Sales')  
plt.xlabel('Discount')  
plt.ylabel('Sales')  
plt.show()


# ### Distribution of Discount v/s Profit

# In[27]:


# Plotting the distribution of Discount
df.plot(x='Profit', y='Sales', style='o')
plt.title('Discount vs Profit')  
plt.xlabel('Discount')  
plt.ylabel('Profit')  
plt.show()


# # ---------------------------------- End of Code ---------------------------------

# In[ ]:




