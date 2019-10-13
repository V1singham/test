# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:33:09 2019

@author: computer zone
"""

t=int(input())
while t:
    t=t-1
    n,m,k=map(int,input().split())
    a=[[0]*m]*n
    
    for i in range(n):
        for j in range(m):
            a[i][j]=0
    a[2][2]=5
    print(a[2][2])        
    for i in range(n):
        for j in range(m):
            print(a[i][j])    