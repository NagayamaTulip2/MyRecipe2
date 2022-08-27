#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def tag2():
    tag2 = ["chiyuri.tiyuri", "tiyuri.chiyuri", "chiyuri_tiyuri", "tiyuri_chiyuri"]
    return random.choice(tag2)
title1 = tag2()

def tag2():
    tag2 = ["chiyuri.chiyuri", "tiyuri.tiyuri", "chiyuri_chiyuri", "tiyuri_tiyuri"]
    return random.choice(tag2)
title2 = tag2()

def tag3():
    tag3 = ["chiyuri.chiyuri.tiyuri", "chiyuri.tiyuri.chiyuri", "tiyuri.chiyuri.chiyuri"
            "chiyuri_chiyuri_tiyuri", "chiyuri_tiyuri_chiyuri", "tiyuri_chiyuri_chiyuri"]
    return random.choice(tag3)
title3 = tag3()

def tag4():
    tag4 = ["tiyuri.tiyuri.chiyuri", "tiyuri.chiyuri.tiyuri", "chiyuri.tiyuri.tiyuri"
            "tiyuri_tiyuri_chiyuri", "tiyuri_chiyuri_tiyuri", "chiyuri_tiyuri_tiyuri"]
    return random.choice(tag4)
title4 = tag4()

def tag5():
    tag5 = ["chiyuri.chiyuri.chiyuri", "chiyuri_chiyuri_chiyuri"]
    return random.choice(tag5)
title5 = tag5()

def tag6():
    tag6 = ["tiyuri.tiyuri.tiyuri", "tiyuri_tiyuri_tiyuri"]
    return random.choice(tag6)
title6 = tag6()

print(title1, title2, title3, title4, title5, title6)

# In[ ]:




