# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 22:39:15 2022

@author: Shilpa
"""

num = list(range(10))
previousNumber=0
for i in num:
    sum=previousNumber+i
    print('CurrentNumber ' + str(i) + ' previousNumber ' + str(previousNumber)+ ' sum is ' + str(sum)) 
    previousNumber=i
    