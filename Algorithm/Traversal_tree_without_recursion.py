#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 16:45:23 2019

@author: gregorywu
"""

import re


class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def inorder_search(root):
    '''left->root->right'''
    current_root = root
    stack = []
    traversal = ''
    
    while True:
        
        if current_root is not None:
            
            stack.append(current_root)
            current_root = current_root.left
            
        elif stack:
            
            current_root = stack.pop()
            traversal += str(current_root.value) + '-'
            
            current_root = current_root.right
            
        else:
            break
        
    return re.sub('-$','',traversal)
    



    
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 


inorder_search(root)