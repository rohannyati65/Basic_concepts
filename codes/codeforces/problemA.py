# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:38:37 2021

@author: Rohan
"""

import math

t=int(input())
i=0
while(i!=t):
    n=int(input())
    k=math.gcd(n,100)
    print(k)
    i+1
