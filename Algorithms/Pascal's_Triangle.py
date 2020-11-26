# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:28:13 2020

@author: popeg


From a Pascal's triangle, retrieve a nth row and print it out.
A Pascal's trigangle is like the following graph:
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1
...


"""


def PascalTriagle(row_n):
    # O(n^2) Time | O(1) Space
    '''
    add a zero_pad
    
    121 0 0 121
    
    1331 0 0 1331
    
    14641 0 0 14641
    
    '''
    
    if row_n == 0:
        return print([1])
    row_value = [1]
    pad = [0]
    
    for i in range(row_n):
        row_value = [left + right for left,right in zip(row_value + pad, pad + row_value)]
        
    print(row_value)
    
   
    
PascalTriagle(7)

    
