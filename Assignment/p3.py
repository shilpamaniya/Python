# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 07:01:22 2022

@author: Shilpa
"""
def printEventIndex (str):
    for i in range(0,len(str)-1,2):
        print("index [",i,"]",str[i])
inputstring=input("enter the string")
print("Original string is",inputstring)
print("event index chars display")
printEventIndex(inputstring)