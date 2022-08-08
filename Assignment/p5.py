# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:18:16 2022

@author: Shilpa
"""

list1 = [0, 1, 2, 3, 4, 5, 6,7]
list2 = [0, 11, 12, 13, 14, 15, 16,17]
res = list()
print("orignal first list",list1)
print("orignal second list",list2)

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index position from list two")
print(even_elements)

print("third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)