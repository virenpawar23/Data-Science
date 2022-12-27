#!/usr/bin/env python
# coding: utf-8

# The `netflix` dictionary contains a list of 100 titles along with their total number of views in the past. Based on the keys and values provided in this dictionary, answer the questions given below.

# In[2]:


netflix = {'The Debt Collector': 1821195, 'Act of Vengeance': 2804479, 'Paradise Lost': 2195477, "Gerald's Game": 3650626, 'Long Shot': 638440, 'Mak Cun': 1010311, 'Our Souls at Night': 3028705, 'Out of Thin Air': 2681938, "Paul Hollywood's Big Continental Road Trip": 230689, 'Satu Hari': 1012350, 'Monster High: Boo York, Boo York': 1526025, 'Cultivating the Seas: History and Future of the Full-Cycle Cultured Kindai Tuna': 2762103, 'Domino': 872663, 'TUNA GIRL': 2574816, '5CM': 2647713, 'Animal World': 220789, 'Hold the Dark': 2307432, 'Lessons from a School Shooting: Notes from Dunblane': 2419534, 'Made in Mexico': 3653712, 'Single': 239278, 'The 3rd Eye': 196138, 'The Sinking Of Van Der Wijck': 2831856, 'Two Catalonias': 1337119, 'Bobby Sands: 66 Days': 2005623, 'Bard of Blood': 744998, 'Deliha 2': 3638900, 'Dragons: Rescue Riders': 3241239, 'In the Shadow of the Moon': 1213329, 'Skylines': 1840094, 'Sturgill Simpson Presents Sound & Fury': 1915540, 'The Politician': 1019394, 'Weeds on Fire': 2273090, 'Much Loved': 3039852, 'Joseph: King of Dreams': 1734449, 'Malaal': 1926128, 'The Grandmaster': 2549410, 'The Inmate': 130965, 'The Hurricane Heist': 2191538, 'Def Comedy Jam 25': 1392697, 'Restless Creature: Wendy Whelan': 2474412, 'Print the Legend': 548250, 'Birders': 3478883, 'Furie': 2755115, 'Leap!': 1401638, 'Oh! Baby (Malayalam)': 839139, 'Oh! Baby (Tamil)': 2691505, 'USS Indianapolis: Men of Courage': 3286014, 'A Wrinkle in Time': 1258861, 'Teach Us All': 2428947, 'White Island': 1152905, 'Inside Man: Most Wanted': 2812661, 'Jeff Dunham: Beside Himself': 2930368, 'China Salesman': 3377292, 'Swearnet: The Movie': 949689, 'The Bar': 620655, 'Manmadhudu 2': 1842761, 'Team Kaylie': 359856, 'Under the Eiffel Tower': 2298237, 'Audrie & Daisy': 1573055, 'Iliza Shlesinger: Confirmed Kills': 365220, 'BONDING': 1664242, 'Do Paise Ki Dhoop Chaar Aane Ki Baarish': 2770879, '20 Feet From Stardom': 2931730, 'In Darkness': 3248749, 'Gaga: Five Foot Two': 3719550, 'The Bad Batch': 3656264, 'SMOSH: The Movie': 3697506, 'King of Boys': 584112, 'Merry Men: The Real Yoruba Demons': 2035595, "Sarah's Key": 1337902, 'The Wedding Party 2: Destination Dubai': 1471204, 'Vagabond': 1600432, 'Battlefish': 723021, 'DRAGON PILOT: Hisone & Masotan': 602919, 'Hilda': 54948, 'Maniac': 1348196, 'Quincy': 2601704, 'Rafinha Bastos: Ultimatum': 3469996, 'The Good Cop': 2265521, 'Between Two Ferns: The Movie': 3146508, 'Criminal: France': 2021409, 'Criminal: Germany': 658824, 'Criminal: Spain': 3078634, 'Criminal: UK': 2721398, 'Daddy Issues': 2119035, "Inside Bill's Brain: Decoding Bill Gates": 1755104, 'The Hockey Girls': 2000507, 'Travel Mates 2': 707260, 'True: Tricky Treat Day': 3213199, 'Two Sentence Horror Stories': 2438329, 'Mad World': 2281773, 'Mobile Suit Gundam UC': 778879, 'The Bund': 1729892, 'The First Line': 674591, 'Maynard': 84986, 'Monkey Twins': 3277179, 'Bitcoin Heist': 1450158, 'I Am Not Madame Bovary': 2763830, 'Vincent N Roxxy': 1961810, "Chef's Table: France": 2065738}


# #### Q1. There's an Indian movie in the dictionary named `Do Paise Ki Dhoop Chaar Aane Ki Baarish`. What is the number of views for this movie?
# - 90,854
# - 658,824
# - 1,023,597
# - 2,770,879

# In[3]:


netflix['Do Paise Ki Dhoop Chaar Aane Ki Baarish']


# #### Q2. Which of the shows is the most and least popular in terms of number of views? </br> 
# (Hint: Use the `key` argument in the max() and min() functions.)
# - Monkey Twins, Maynard
# - Gaga: Five Foot Two, Hilda
# - Gerald's Game, White Island
# - Rafinha Bastos: Ultimatum, The First Line

# In[7]:


max(netflix,key=netflix.get)


# In[9]:


min(netflix,key=netflix.get)


# Netflix has just recieved the number of views for the last week as well. This data is given below, in the form of a dictionary

# In[10]:


netflix_last_week = {'The Debt Collector': 229218, 'Act of Vengeance': 191468, 'Paradise Lost': 167846, "Gerald's Game": 113298, 'Long Shot': 15190, 'Mak Cun': 244581, 'Our Souls at Night': 188095, 'Out of Thin Air': 183961, "Paul Hollywood's Big Continental Road Trip": 207967, 'Satu Hari': 226211, 'Monster High: Boo York, Boo York': 265919, 'Cultivating the Seas: History and Future of the Full-Cycle Cultured Kindai Tuna': 192246, 'Domino': 190538, 'TUNA GIRL': 301819, '5CM': 154371, 'Animal World': 228227, 'Hold the Dark': 222938, 'Lessons from a School Shooting: Notes from Dunblane': 256580, 'Made in Mexico': 199790, 'Single': 155517, 'The 3rd Eye': 251349, 'The Sinking Of Van Der Wijck': 153797, 'Two Catalonias': 189422, 'Bobby Sands: 66 Days': 202461, 'Bard of Blood': 241928, 'Deliha 2': 304552, 'Dragons: Rescue Riders': 155149, 'In the Shadow of the Moon': 222999, 'Skylines': 118737, 'Sturgill Simpson Presents Sound & Fury': 43590, 'The Politician': 11902, 'Weeds on Fire': 243382, 'Much Loved': 190123, 'Joseph: King of Dreams': 46104, 'Malaal': 70961, 'The Grandmaster': 44908, 'The Inmate': 19574, 'The Hurricane Heist': 167696, 'Def Comedy Jam 25': 208075, 'Restless Creature: Wendy Whelan': 22976, 'Print the Legend': 161584, 'Birders': 257668, 'Furie': 282266, 'Leap!': 124338, 'Oh! Baby (Malayalam)': 18203, 'Oh! Baby (Tamil)': 131481, 'USS Indianapolis: Men of Courage': 76558, 'A Wrinkle in Time': 169365, 'Teach Us All': 50378, 'White Island': 299779, 'Inside Man: Most Wanted': 123346, 'Jeff Dunham: Beside Himself': 283561, 'China Salesman': 182041, 'Swearnet: The Movie': 63809, 'The Bar': 41243, 'Manmadhudu 2': 261349, 'Team Kaylie': 101283, 'Under the Eiffel Tower': 83650, 'Audrie & Daisy': 106092, 'Iliza Shlesinger: Confirmed Kills': 255103, 'BONDING': 202683, 'Do Paise Ki Dhoop Chaar Aane Ki Baarish': 32329, '20 Feet From Stardom': 165178, 'In Darkness': 95259, 'Gaga: Five Foot Two': 36638, 'The Bad Batch': 197820, 'SMOSH: The Movie': 196519, 'King of Boys': 49332, 'Merry Men: The Real Yoruba Demons': 293229, "Sarah's Key": 178523, 'The Wedding Party 2: Destination Dubai': 51211, 'Vagabond': 116831, 'Battlefish': 5448, 'DRAGON PILOT: Hisone & Masotan': 281873, 'Hilda': 21348, 'Maniac': 268187, 'Quincy': 139696, 'Rafinha Bastos: Ultimatum': 105449, 'The Good Cop': 73230, 'Between Two Ferns: The Movie': 135600, 'Criminal: France': 243469, 'Criminal: Germany': 285211, 'Criminal: Spain': 45184, 'Criminal: UK': 117056, 'Daddy Issues': 267329, "Inside Bill's Brain: Decoding Bill Gates": 64083, 'The Hockey Girls': 114146, 'Travel Mates 2': 21088, 'True: Tricky Treat Day': 116504, 'Two Sentence Horror Stories': 274471, 'Mad World': 225244, 'Mobile Suit Gundam UC': 47306, 'The Bund': 146872, 'The First Line': 148861, 'Maynard': 87252, 'Monkey Twins': 199274, 'Bitcoin Heist': 41105, 'I Am Not Madame Bovary': 57841, 'Vincent N Roxxy': 207453, "Chef's Table: France": 200536}


# #### Q3. Netflix has just recieved the number of views for the last week as well. Add these views to the total views and find the most popular title in terms of views. Also find out how many views this title has? 
# - Title: Deliha 2, Views: 3943452
# - Title: Dragons: Rescue Riders, Views: 3996388
# - Title: Rafinha Bastos: Ultimatum, Views: 3575445
# - Title: Gaga: Five Foot Two, Views: 3756188

# In[18]:


from collections import Counter
new_netflix = Counter(netflix_last_week)+Counter(netflix)


# In[22]:


max(new_netflix,key=new_netflix.get),new_netflix[max(new_netflix,key=new_netflix.get)]


# In[ ]:




