#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def tag():
    tag = ["work", "experiment", "room", "home", "walking", "science", "lifestyle", "city", "park",
          "color", "nature", "dynamics", "sea", "summer", "neon", "urban", "fireworks", "light", "flower",
          "forest", "spectral", "world", "architecture", "rainbow", "tulip"]
    return random.choice(tag)
title = tag()

print(title + "が今回のキーワードです。")

# In[ ]:




