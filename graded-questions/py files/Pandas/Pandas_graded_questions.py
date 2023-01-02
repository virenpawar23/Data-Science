#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df_sales = pd.read_csv("MegaMart_sales.csv")


# In[3]:


df_newsales = pd.read_csv("MegaMart_newsales.csv")


# In[4]:


combined = df_sales.append(df_newsales)
len(combined)


# In[5]:


combined


# In[6]:


combined.columns


# 
# 

# ## 1. Combining two data frames
# Some of the orders are stored in another csv file named `megamart_new sales`. Read the csv file, store it in a data frame and add it to the `megamart_sales` data frame.

# Question 1: Find the total sales value of the category 'Office Supplies'  after combining the dataframes
# 
#     a)7970
#     b)6964
#     c)7494
#     d)6076

# In[7]:


combined["Category"].unique()


# In[8]:


combined[combined["Category"]=="Office Supplies"]["Sales"].sum()


# ----------

# ## 2. Dropping duplicates
# Question 2: There are some duplicate rows in the data frame. Drop these rows and calculate the total sales value of the category Office Supplies.
# 
#     a)7156
#     b)6496
#     c)6964
#     d)6023

# In[9]:


combined_no_dups = combined.drop_duplicates()
len(combined_no_dups)


# In[10]:


combined_no_dups[combined_no_dups["Category"]=="Office Supplies"]["Sales"].sum()


# -------

# -----

# ## 3. Best category-sub category 
# Question 3: Find the most profitable category and sub category combination based on the net profit.
# 
# 
#     a)Furniture-Bookcases
#     b)Office supplies-Appliances
#     c)Office supplies-Storage
#     d)Technology-Phones

# In[11]:


grp_cat_subcat_mean = combined.groupby(["Category","Sub-Category"])["Profit"].sum()
grp_cat_subcat_mean


# In[12]:


grp_cat_subcat_mean.sort_values(ascending=False).head(1)


# ---------

# ## 4. Invalid order IDs
# Question 4: How many invalid order IDs are there in the data frame? An order id is of the form AZ-2011-Y where Y represents a whole number. A Order ID is said to be valid only if Y consists of 7 digits. Find the number of invalid order IDs in the data frame.
#     
#     a)6
#     b)7
#     c)8
#     d)9
# 

# In[13]:


def check_order_id(order_id):
    y = order_id.split("-")[-1]
    if (y.isdigit()) and (len(y)==7):
        return False
    else:
        return True
invalid_order_ids = combined_no_dups["Order ID"].apply(check_order_id)
combined_no_dups["Order ID"][invalid_order_ids]


# In[14]:


len(combined_no_dups["Order ID"][invalid_order_ids])


# --------

# ## 5. Occurence of furniture in top 25 sales
# Question 5: Find the top 25 orders based on sales value and find the number of orders which belong to furniture category.
# 
#     a)2
#     b)3
#     c)4
#     d)5 

# In[15]:


top25 = combined_no_dups.sort_values(by="Sales",ascending=False)[:25]
top25[top25["Category"]=="Furniture"]


# In[16]:


top25["Category"].value_counts()


# --------------------------------

# ## 6. And operation
# Question 6: Among the orders with sales>250 and profit>50, find the product name of the fourth highest order based on sales value.
# 
#     a)Motorola Headset, with Caller ID
#     b)Panasonic Printer, Durable	
#     c)Hoover Microwave, Red	
#     d)Fellowes Lockers, Industrial	

# In[17]:


combined_no_dups[(combined_no_dups["Sales"]>250) & (combined_no_dups["Profit"]>50)].sort_values(by="Sales",ascending=False)["Product Name"].iloc[3]


# ## 7. Column manipulation
# Question 7: Remove the orders with negative profit by dropping the corresponding rows with negative `Profit`. Find the product that makes the lowest profit per Quantity in the Technology category.
# 
#     a) Nokia Audio Dock, with Caller ID
#     b) Logitech Keyboard, Programmable
#     c) Motorola Headset, with Caller ID
#     d) Belkin Flash Drive, Bluetooth

# In[18]:


# combined_no_dups.assign(Profit_per_qty=0)  # creates a column with default values
df_positive_profit = combined_no_dups[combined_no_dups["Profit"]>0]
df_positive_profit_tech = df_positive_profit[df_positive_profit["Category"]=="Technology"]
# df_positive_profit_tech_cp = df_positive_profit_tech.copy()
df_positive_profit_tech["Profit per qty"] = df_positive_profit_tech["Profit"]/df_positive_profit_tech["Quantity"]
df_positive_profit_tech.sort_values(by="Profit per qty").head(1)


# In[ ]:




