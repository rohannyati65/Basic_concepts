# -*- coding: utf-8 -*-
"""p1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p2mAv1q48qUedSRisLlOLo0-L21KioGJ
"""

t=int(input())
while(t!=0):
    sum=0
    n=int(input())
    if(n<9):
        print(0)
    else:
        for i in range(9,n+1,++10):
            sum=sum+1
        print(sum)
    
    t=t-1