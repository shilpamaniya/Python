# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 19:19:57 2022

@author: Shilpa
"""

lower=1
upper=5

print("prime numbers between",lower,"and ",upper)
for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                break
            else:
                print(num)