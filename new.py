#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:03:12 2020

@author: fed
"""


def Fibonacci_number(n):
    if n<=0:
        print("Incorrecto")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci_number(n-1)+Fibonacci_number(n-2)
 
if __name__ == "__main__":
 
    print(Fibonacci_number(19))