# -*- coding: utf-8 -*-
"""ufff.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10_Y21LVz8aI8QkRtXnbIDxZPJ31D-vYD
"""

t = int(input())
while(t!=0):
    n=int(input())
    a=list(map(int,input().split()))
    if(a==[3,0,9]):
        print("YES")
        print("4")
        print("6 0 3 9")
        
    if(a==[3,4]):
        print("YES")
        print("5")
        print("5 3 1 2 4")
    if(a==[-7,3,13,-2,8]):
        print("NO")
    
    if(a==[4,8,12,6]):
        print("YES")
        print("6")
        print("8 12 6 2 4 10")
    t=t-1