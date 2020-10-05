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
  

def Max_elements(list1, N): 
    f = [] 
  
    for i in range(0, N):  
        max1 = 0
          
        for j in range(len(list1)):      
            if list1[j] > max1: 
                max1 = list1[j]; 
                  
        list1.remove(max1); 
        f.append(max1) 
          
    return f
  




if __name__ == "__main__":
    
    
    list1 = [22, 62, 412, 825, 12, 345, 47, 56, 140] 
    N = 3
      
    # Calling the function 
    Max_elements(list1, N) 
    

    arr = [ 130, 100, 15, 5, 345, 140 ] 
    lens = len(arr) 
    n = 11
      

    print( remainder(arr, lens, n))  



    for i in range(1,10):
        print(Fibonacci_number(i))