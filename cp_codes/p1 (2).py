# -*- coding: utf-8 -*-
"""p1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p2mAv1q48qUedSRisLlOLo0-L21KioGJ
"""

t=int(input())
while(t!=0):
    n=int(input())
    if(n<9):
        print(0)
    
    elif(n==9):
        print(1)
        
    else:
        a=str(n)
        l=[int(i) for i in a]
        if(l[-1]==9):
            x=(n//10)
            print(int(x)+1)
        else:
            x=(n//10)
            print(int(x))
    t=t-1