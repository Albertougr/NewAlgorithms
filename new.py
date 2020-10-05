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
 
    
 
    
def remainder(arr, lens, n): 
    mul = 1
  
    for i in range(lens):  
        mul = (mul * (arr[i] % n)) % n 
      
    return mul % n 
  




if __name__ == "__main__":

    arr = [ 130, 100, 15, 5, 345, 140 ] 
    lens = len(arr) 
    n = 11
      
    print( remainder(arr, lens, n))  



    for i in range(1,10):
        print(Fibonacci_number(i))