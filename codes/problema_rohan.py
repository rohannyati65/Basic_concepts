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
    s=list(map(int,s1))
    lst=list(map(int,s1))
    #print(s)
    #print(type(n))
    #print(m)
    #print(s)
    for j in range(int(m)):
        #s=lst
        #print(s)
        for i in range(0,int(n)):
            #print(i)
            #print("h1")
            if(i==0):
                if(s[i]==0):
                    if(s[i+1]==1):
                        #print("h2")
                        #s.replace(s[i],1)
                        lst[i]=1
                        pass
            if(i==(int(n)-1)):
                if(s[i]==0):
                    if(s[i-1]==1):
                        #s.replace(s[i],1)
                        lst[i]=1
                        pass
            else:
                if(s[i]==0):
                    if(s[i+1]==1):
                        if(s[i-1]!=1):
                            #s.replace(s[i],1)
                            lst[i]=1
                            pass
                        #else:
                        #    s[i]=0
                    if(s[i-1]==1):
                        if(s[i+1]!=1):
                            #s.replace(s[i],1)
                            lst[i]=1
                            pass
            #print(lst)    
            #print(s)
            #else:
                        #    s[i]=0
        #print(lst)
        s=list(lst)
        #print(s)
    res = str("".join(map(str, lst)))
    #x=str(res)
    #s2=""
    #s3=s2.join(s)
    print(res)
    #print(type(x))
    t=t-1