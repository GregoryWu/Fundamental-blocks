# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 10:34:48 2021

@author: popeg
"""

def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    # trace back to where the cycle began
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1

print(findDuplicate([4,1,2,3,4,0]))
