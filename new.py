#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:03:12 2020

@author: fed
"""



def Fibonacci_number(n):
    if n<=0:
        print("Incorrect")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        #recursive
        return Fibonacci_number(n-1)+Fibonacci_number(n-2)
 
    
 
    
def remainder(arr, lens, n): 
    mul = 2
  
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
  
    c = {} 
      
    for w in A.split(): 
        c[w] = c.get(w, 0) + 1
      
    for w in B.split(): 
        
        c[w] = c.get(w, 0) + 1
  
    return [w for w in c if c[w] == 1] 
  


def moreK(k, str): 
      
    s = [] 
      
    text = str.split(" ") 
      
    for t in text: 
        if len(t) > k: 
              
            s.append(t) 
    return s 
  
  
  

def has_all(string) : 
  
    s = string.lower() 
    v = set("aeiou") 
  
    s = set({}) 
  
    for c in s : 
        if c in v : 
            s.add(c) 
        else: 
            pass
              
    if len(s) == len(v) : 
        print("good") 
    else : 
        print("Not good") 
  
  
      

if __name__ == "__main__":
    
    
    
    
    k2 = 3
    str ="esto es una prueba"
    print(moreK(k2, str))
        
        
    s = "nosesitieneull"
    has_all(s) 
    
    
    
    
    ###################################3
    
    list1 = [222, 62, 412, 8252, 12, 345, 47, 56, 140] 
    N = 4
      
    # Calling the function 
    Max_elements(list1, N) 
    

    arr = [ 1330, 100, 15, 5, 3435, 140 ] 
    arer = [ 1330, 100, 15, 5, 3435, 140 ] 

    lens = len(arr) 
    n = 12
      

    print( remainder(arr, lens, n))  



    for i in range(1,14):
        print(Fibonacci_number(i))
        
        
    stringA = "eran uno dos y tres"
    stringB = "tres triste tigres eran dos ??"
      
    # Print required answer 
    print(PalabrasNoComunes(stringA, stringB)) 