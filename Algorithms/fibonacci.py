#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:36:58 2019

@author: gregorywu
"""


# Recursive method
# T = O(2**n)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    
    else:
        return fibonacci(n-2) + fibonacci(n-1)
        
for n in range(1,50):
    print(n,":", fibonacci(n))
 
    
# Dynamic approach 
    
# [1] Memoization
# T = O(2N+1) = O(2N)

fibonacci_cache = {}

def fib_with_memo(n):
    
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    if n == 1 or n == 2:
        value = 1
    

    else:
        value = fib_with_memo(n-2) + fib_with_memo(n-1)
    
    fibonacci_cache[n] = value
    
    return value
    
for n in range(1,500):
    print(n,":", fib_with_memo(n)) 
    
    
# [2] bottom-up
# T = O(N)

def fib_bottom_up(n):
    if n ==0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    bottom_up = [None] * (n+1)
    
    bottom_up[1] = 1 
    bottom_up[2] = 1 
    
    for i in range(3,n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    
    return bottom_up[n]
    
for n in range(1,500):
    print(n,":", fib_bottom_up(n)) 


