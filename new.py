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
  



def PalabrasNoComunes(A, B): 
  
    # count will contain all the word counts 
    count = {} 
      
    # insert words of string A to hash 
    for w in A.split(): 
        count[w] = count.get(w, 0) + 1
      
    # insert words of string B to hash 
    for w in B.split(): 
        count[w] = count.get(w, 0) + 1
  
    # return required list of words 
    return [w for w in count if count[w] == 1] 
  




if __name__ == "__main__":
    
    
    list1 = [222, 62, 412, 825, 12, 345, 47, 56, 140] 
    N = 4
      
    # Calling the function 
    Max_elements(list1, N) 
    

    arr = [ 1330, 100, 15, 5, 345, 140 ] 
    lens = len(arr) 
    n = 11
      

    print( remainder(arr, lens, n))  



    for i in range(1,14):
        print(Fibonacci_number(i))
        
        
    A = "eran uno dos y tres"
    B = "tres triste tigres eran dos"
      
    # Print required answer 
    print(PalabrasNoComunes(A, B)) 