#!/usr/bin/env python
# coding: utf-8

# In a school, there are total 100 students numbered from 1 to 100. You’re given three lists named ‘C’, ‘F’, and ‘H’, representing students who play cricket, football, and hockey, respectively. Based on this information, find out and print the following: 
# - Students who play all the three sports
# - Students who play both cricket and football but don’t play hockey
# - Students who play exactly two of the sports
# - Students who don’t play any of the three sports

# In[24]:


Crick = [7, 8, 9, 18, 20, 21, 25, 26, 27, 31, 32, 34, 35, 36, 40, 43, 45, 47, 53, 58, 62, 67, 68, 71, 72, 74, 75, 76, 80, 81, 82, 90, 93, 95, 97, 99]
Foot = [1, 7, 10, 13, 16, 22, 24, 29, 30, 32, 34, 39, 40, 43, 44, 48, 56, 60, 65, 68, 69, 73, 77, 78, 90, 93, 94, 95, 96]
Hock = [5, 12, 14, 17, 20, 21, 22, 25, 28, 30, 37, 38, 39, 40, 42, 44, 57, 59, 61, 62, 67, 71, 75, 76, 77, 82, 83, 86, 87, 92, 94, 95]


# In[25]:


C = set(Crick)
F = set(Foot)
H = set(Hock)


# #### Q1. Which are the students who play all the three sports?
# - [22, 39]
# - [39, 82]
# - [40, 95]
# - [82, 94]

# In[28]:


C&F&H


# #### Q2. Which are the players who play both cricket and hockey but don't play football?
# - [20, 21, 25, 62, 67, 71, 75, 76, 82]
# - [20, 21, 22, 25, 30, 32, 34]
# - [20, 21, 22, 25, 30, 32, 34, 39, 43, 44, 62]
# - [20, 21, 68, 71, 75, 76]

# In[30]:


(C&H)-F


# #### Q3. How many players play exactly two sports?
# - 19
# - 20
# - 21
# - 22

# In[39]:


len(
    (
        (C&H)-F
    ).union(
        (C&F)-H
    ).union(
        (H&F)-C
    )
)


# In[43]:


len((C&H)-F | (C&F)-H | (F&H)-C)


# #### Q4. Which of these students do not play any of the sports? (More than one option may be correct)
# - 41
# - 48
# - 63
# - 85

# In[49]:


A = set(range(1,101))
len(A)


# In[51]:


len(A-(C|H|F))


# In[53]:


for i in [41,48,63,85]:
    if i in A-(C|H|F):
        print(i)


# In[54]:


A-(C|H|F)


# In[ ]:




