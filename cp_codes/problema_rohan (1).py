# -*- coding: utf-8 -*-
"""ProblemA_ROHAN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1586HMpEgIPpGwMsyhQ5Kn0mMlfoTOV3d
"""

t = int(input())

while(t!=0):
    n,m=input().split()
    s1=str(input())
    lst=list(map(int,s1))
    s=list(lst)
    for j in range(int(m)):
        for i in range(0,int(n)):
            if(i==0):
                if(s[i]==0):
                    if(s[i+1]==1):
                        lst[i]=1
                        pass
            if(i==(int(n)-1)):
                if(s[i]==0):
                    if(s[i-1]==1):
                        lst[i]=1
                        pass
            else:
                if(s[i]==0):
                    if(s[i+1]==1):
                        if(s[i-1]!=1):
                            lst[i]=1
                            pass
                    if(s[i-1]==1):
                        if(s[i+1]!=1):
                            lst[i]=1
                            pass
        s=list(lst)
    res = str("".join(map(str, lst)))
    print(res)
    t=t-1