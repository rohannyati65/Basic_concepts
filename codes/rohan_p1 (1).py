# -*- coding: utf-8 -*-
"""rohan_p1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Tps7xXEJOnPkuQ5b-p7ExChD42dutQ3T
"""

t=int(input())
while(t!=0):
    n=int(input())
    a=(n/3)
    b=int(a)
    c1=abs(b+1)
    c2=abs(b-1)
    l=[c1,b]
    l.sort()
    l=l[::-1]
    l1=[c2,b]
    l1.sort()
    l1=l[::-1]
    l2=[b,b]
    if(l[0]+(2*l[1])==n):
        print(*l)
    
    if(l1[0]+(2*l1[1])==n):
        print(*l1)
    
    if(l2[0]+(2*l2[1])==n):
        print(*l2)
    t=t-1