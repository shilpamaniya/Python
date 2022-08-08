# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:41:26 2022

@author: Shilpa
"""

demolist=[16,12,2000,2001,22,1,2002,24,1,2004]
print("original list",demolist);

removelist=demolist.pop(4)
print("after remove element in the index4")
print(removelist)

demolist.insert(2,removelist)

print("element add in the second position")
print(demolist)

demolist.append(removelist)
print("after completed all..",demolist)