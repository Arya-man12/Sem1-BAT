# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 22:10:38 2023

@author: Aryaman Kumar
"""
#Program to distinguish between primitive and compound data type
a=eval(input("Enter input"))
print(a)
print(type(a))
if(type(a) in [list,tuple,dict,set]):
    print("Compound data type")
else:
    print("Primitive data type")
print("Name-Aryaman Kumar,registration no-22BRS1184")
    