# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:39:20 2019

@author: computer zone
"""

t=int(input())
for i in range(t):
    n=int(input())
   # a=list(n)
    a=[n]
   # a.len()=n
    s=0
    a1=-1
    a,c=input().split()
    
    for i in range(n):
        if a[i]==c:
            x1=i-(a1+1)
            x2=n-(a1+1)
            s=s+(x2-x1)*x1+(x2-x1)
            a1=i
    print(s)        
    
    