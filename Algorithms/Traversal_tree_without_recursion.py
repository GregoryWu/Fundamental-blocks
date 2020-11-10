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
    
    

def peek(stack): 
    if len(stack) > 0: 
        return stack[-1] 
    return None


def postorder_search_1_stack(root):
    
    stack = []
    ans = []

    
    while True:
        
        
        while root:
            
            if root.right is not None:
                stack.append(root.right) # Push root's right child and then root to stack.
            stack.append(root) # Set root as root's left child.
            root = root.left
    
    
        root = stack.pop()
        
        # If the popped item has a right child and the right child 
        # is at top of stack, then remove the right child from stack,
        # push the root back and set root as root's right child.
        if root.right is not None and root.right == peek(stack):
            stack.pop()
            stack.append(root)
            root = root.right


        # print root's data and set root as NULL.
        else:
           ans.append(root.value)
           root = None
           
        if (len(stack) <= 0): 
            break

    return '-'.join(map(str, ans))





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





def inorder_MorrisTraversal(root): 
    '''left->root->right'''
    
    # Set current to root of binary tree 
    current = root  
      
    traversal = ''
    
    while current: 
          
        if current.left is None: 
            
            traversal += str(current.value) + '-'
            
            current = current.right 
            
            
        else: 
            # Find the inorder predecessor of current 
            pre = current.left 
            
            
            # Make current as the right child of the rightmost 
            # node in current's left subtree
            while pre.right is not None and pre.right != current: 
                pre = pre.right 
   

            if pre.right is not None: 
                
                pre.right = None
                traversal += str(current.value) + '-'
                current = current.right 
                  
            else: 
                pre.right = current 
                current = current.left 

    return re.sub('-$','',traversal)

    


def preorder_MorrisTraversal(root): 
    '''root->left->right'''
    
    current = root 
  
    traversal = ''
    
    while current: 

        if current.left is None: 
            
            traversal += str(current.value) + '-'
            current = current.right 
  
        else: 

            pre = current.left 
  
    
            # Make current as the right child of the rightmost 
            # node in current's left subtree
            while pre.right is not None and pre.right is not current: 
                pre = pre.right 
  
    
    
            if pre.right is current: 
                pre.right = None
                current = current.right 
                  

            else: 
                traversal += str(current.value) + '-'
                pre.right = current  
                current = current.left 
                
    return re.sub('-$','',traversal)


def postorder_MorrisTraversal(root):
    '''left->right->root'''
    
    if not root:
        return []
    current = root
    post_order_list = []
    
    while current:
        
        if not current.right:
            post_order_list.insert(0, current.value)
            current = current.left
            
        else:
            # find leftmost of the right sub-tree
            pre = current.right
            while pre.left is not None and pre.left != current:
                pre = pre.left
                
                
            # and create a link from this to current
            if pre.left:
                pre.left = None
                current = current.left

                
            else:
                post_order_list.insert(0, current.value)
                pre.left = current
                current = current.right
                
    return '-'.join(map(str, post_order_list))


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

postorder_MorrisTraversal(root)



# Preorder traversal 
preorder_search_1_stack(root)
preorder_MorrisTraversal(root)

