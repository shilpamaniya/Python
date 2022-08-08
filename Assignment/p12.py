# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:33:37 2022

@author: Shilpa
"""


List1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in range(0, len(List1), 1):

    if List1[i]<=150:
    
        if List1[i]%5==0:
    
            print(List1[i])