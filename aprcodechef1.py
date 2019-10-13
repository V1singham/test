# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:21:50 2019

@author: computer zone
"""

n=int(input())
a=[n]
a=list(map(int,input().split()))
a.sort()
x1=a[n-1]
x2=0
for i in range(n):
    if a[n-1-i]<x1:
        x2=a[n-1-i]
        break
d=int(x2%x1)    
print(d)    