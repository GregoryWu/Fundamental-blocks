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
    current = root
    stack = []
    traversal = ''
    
    while True:
        
        if current is not None:
            
            stack.append(current)
            current = current.left
            
        elif stack:
            
            current = stack.pop()
            traversal += str(current.value) + '-'
            
            current = current.right
            
        else:
            break
        
    return re.sub('-$','',traversal)
    
## TODO
def inorder_MorrisTraversal(root): 
    '''left->root->right'''
    
    # Set current to root of binary tree 
    current = root  
      
    traversal = ''
    
    while(current is not None): 
          
        if current.left is None: 
            
            traversal += str(current.value) + '-'
            
            current = current.right 
        else: 
            # Find the inorder predecessor of current 
            pre = current.left 
            
            while(pre.right is not None and pre.right != current): 
                pre = pre.right 
   
            # Make current as right child of its inorder predecessor 
            if(pre.right is None): 
                pre.right = current 
                current = current.left 
                  
            # Revert the changes made in if part to restore the  
            # original tree i.e., fix the right child of predecessor 
            else: 
                pre.right = None
                
                traversal += str(current.value) + '-'
            
                current = current.right 
    return re.sub('-$','',traversal)



def postorder_search_2_stacks(root):
    '''left->right->root'''
    stack_1 = []
    stack_2 = []
    stack_1.append(root)
    
    traversal = ''
    
    while stack_1:
        
        popped_node = stack_1.pop()
        stack_2.append(popped_node.value)
        
        if popped_node.left:
            stack_1.append(popped_node.left)
        if popped_node.right:
            stack_1.append(popped_node.right)
        
    while stack_2:
        traversal += str(stack_2.pop()) + '-'
  
    return re.sub('-$','',traversal)
    
    
## TODO
ans = [] 
def peek(stack): 
    if len(stack) > 0: 
        return stack[-1] 
    return None
# A iterative function to do postorder traversal of  
# a given binary tree 
def postorder_search_1_stack(root): 
          
    # Check for empty tree 
    if root is None: 
        return 
  
    stack = [] 
      
    while True: 
          
        while root: 
             # Push root's right child and then root to stack 
             if root.right is not None: 
                stack.append(root.right) 
             stack.append(root) 
  
             # Set root as root's left child 
             root = root.left 
          
        # Pop an item from stack and set it as root 
        root = stack.pop() 
  
        # If the popped item has a right child and the 
        # right child is not processed yet, then make sure 
        # right child is processed before root 
        if (root.right is not None and 
            peek(stack) == root.right): 
            stack.pop() # Remove right child from stack  
            stack.append(root) # Push root back to stack 
            root = root.right # change root so that the  
                             # righ childis processed next 
  
        # Else print root's data and set root as None 
        else: 
            ans.append(root.data)  
            root = None
  
        if (len(stack) <= 0): 
                break







def preorder_search_1_stack(root): 
    '''root->left->right'''  

    # create an empty stack and push root to it 
    nodeStack = [] 
    nodeStack.append(root) 
    
    traversal = ''

    while nodeStack: 
          
        # Pop the top item from stack and print it 
        node = nodeStack.pop() 

        traversal += str(node.value) + '-'
          
        # Push right and left children of the popped node 
        # to stack 
        if node.right: 
            nodeStack.append(node.right) 
        if node.left: 
            nodeStack.append(node.left) 


    return re.sub('-$','',traversal)

def preorder_MorrisTraversal(root): 
    curr = root 
  
    while curr: 
        # If left child is null, print the 
        # current node data. And, update  
        # the current pointer to right child. 
        if curr.left is None: 
            print(curr.data, end= " ") 
            curr = curr.right 
  
        else: 
            # Find the inorder predecessor 
            prev = curr.left 
  
            while prev.right is not None and prev.right is not curr: 
                prev = prev.right 
  
            # If the right child of inorder 
            # predecessor already points to 
            # the current node, update the  
            # current with it's right child 
            if prev.right is curr: 
                prev.right = None
                curr = curr.right 
                  
            # else If right child doesn't point 
            # to the current node, then print this 
            # node's data and update the right child 
            # pointer with the current node and update 
            # the current with it's left child 
            else: 
                print (curr.data, end=" ") 
                prev.right = curr  
                curr = curr.left 

# Construct a binary tree
'''
     1
    / \
   2   3
  / \
 4   5
    /
   6
  
'''
    
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.right.left = Node(6) 

# Inorder traversal
inorder_search(root)
inorder_MorrisTraversal(root)


# Postorder traversal
postorder_search_2_stacks(root)
postorder_search_1_stack(root)

# Preorder traversal 
preorder_search_1_stack(root)
preorder_MorrisTraversal(root)

