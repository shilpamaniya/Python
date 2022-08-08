# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 19:11:23 2022

@author: Shilpa
"""

row=int(input("enter the number"))
for i in range(row):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\r")