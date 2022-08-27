#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

num = input("何パターンを作成しますか？")

for i in range(0, int(num)):
    angle = random.sample(range(0, 360), 1)[0]
    angle2 = random.sample(range(-100, 100), 1)[0]
    
    print("直線：" + str(angle) + "°回転、" + str(angle2) + "％カーブ")

for i in range(0, int(num)):
    ratio = random.sample(range(0, 50), 5)
    print(str(ratio))
        
for i in range(0, int(num)):
    r_col = random.sample(range(0, 255), 1)[0]
    g_col = random.sample(range(0, 255), 1)[0]
    b_col = random.sample(range(0, 255), 1)[0]
    
    print("R：" + str(r_col) + " G：" + str(g_col) + " B：" + str(b_col))  


# In[ ]:




