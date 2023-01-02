#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# ## 1. Index of 50th element
# Consider an (8, 8) shape NumPy array. What is the index (x,y) of the 50th element?
# 
# Note: For counting the elements go row-wise. For example, in the array,
# 
# [[1, 5, 9],
# 
#  [3, 0, 2]]
# 
# the 5th element would be '0'.

# In[19]:


df1 = np.arange(1,65).reshape((8,8))


# #### Alternative: 1

# In[17]:


np.argwhere(df1==50)


# #### Alternative: 2

# In[18]:


np.unravel_index(49, (8,8))


# <hr>

# ## 2. Slicing Arrays
# Which of the following would extract all the first 3 rows of the last 5 columns in a given numpy 2D array ‘a’?

# #### Answer: -
# 
# #### a[:3,-5:]

# </hr>

# <hr>

# <hr>

# ## 3. So Many Functions
# What will the output of np.arange(1,16,2).reshape(4, 2) be?

# In[24]:


np.arange(1,16,2).reshape(4, 2)


# <hr>

# ## 4. Coding question

# In[43]:


import numpy as np 

n = int(input())
mid = int(n/2)
df = np.zeros((n,n),dtype=int)
df[mid,:]=df[:,mid]=1
df


# <hr>

# In[ ]:




