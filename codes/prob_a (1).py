# -*- coding: utf-8 -*-
"""prob_a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gP84WGJ-Kwr5NJD1efqaZ2G2CGOb91pF
"""

def min_value(lst,count,a):
    if a in lst:
        d=lst.index(a)
        if(len(lst[:d+1])>len(lst[d:])):
            for i in lst[d:]:
                lst.remove(i)
                count=count+1
            return(count)
        else:
            for i in lst[:d+1]:
                lst.remove(i)
                count=count+1
            return(count)
    else:
        return(count)
    
def max_value(lst,count,b):
    if b in lst:
        e=lst.index(b)
        if(len(lst[:e+1])>len(lst[e:])):
            for i in lst[e:]:
                lst.remove(i)
                count=count+1
            return(count)
        
        else:
            for i in lst[:e+1]:
                lst.remove(i)
                count=count+1
            return(count)
    else:
        return(count)
    
t = int(input())
while(t!=0):
    n=int(input())
    lst=list(map(int,input().split()))
    a=min(lst)
    b=max(lst)
    count=0
    f=lst.index(a)
    g=lst.index(b)
    if(len(lst[:f+1])<len(lst[:g+1])):
        x=min_value(lst,count,a)
        y=max_value(lst,x,b)
        print(y)
    
    else:
        x=max_value(lst,count,b)
        y=min_value(lst,x,a)
        print(y)
    
    t=t-1