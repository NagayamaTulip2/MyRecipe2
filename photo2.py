#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def tag():
    tag = ["colored pencil", "fruit", "ink", "vegetable", "halloween",
           "snack", "bread", "cloud", "amusement park", "festival", "ship",
           "large tree", "rainbow", "water", "waterfall", "rose", "hydrangea",
           "lily", "rainy season", "sakura", "flower garden", "dandelion",
           "park", "trip", "cafe", "hiking", "sunrise", "snow", "ice", "aurora",
           "christmas", "candle", "illumination", "mountain", "sea", "sky", "bird",
           "castle", "starry sky", "autumn", "brick", "moon", "autumn leaves",
           "evening", "meadow", "palm", "night view", "beautiful", "amazing"]
    
    return random.choice(tag)
title = tag()

print(title + "が今回のキーワードです。")

# In[ ]:




