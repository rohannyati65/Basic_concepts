# -*- coding: utf-8 -*-
"""Rohan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18KXfLkackkGCwW57Hl-DZ_mS3pEvjr0i
"""

t = int(input())

def string_creation(s):
    global count
    str1="1"
    for i in range(len(s)-1):
        str1=str1+str(1)
        count=count+1
    return(int(str1))


while(t!=0):
    s=int(input())
    count = 0
    while(1):
        y=string_creation(str(s))
        s=s-y
        if(s<10):
            break
    if(s==0):
        if(count>1):
            print("YES")
        else:
            print("NO")
    if(s!=0):
        print("NO")
    t=t-1