# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:51:30 2019

@author: popeg
"""

import re

class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
        
class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.append(item)
        
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def preorder_search(self, start, traversal=str):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_search(start.left, traversal)
            traversal = self.preorder_search(start.right, traversal)
        print(traversal)
        return traversal

    def inorder_search(self, start, traversal=str):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_search(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_search(start.right, traversal)
        return traversal

    def postorder_search(self, start, traversal=str):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_search(start.left, traversal)
            traversal = self.postorder_search(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def Breadth_first_search(self, start):
        if start is None:
            return 

        queue = Queue()
        queue.enqueue(start)

        traversal = ""

        while len(queue) > 0 :
            traversal += str(queue.peek()) + '-'
            node = queue.dequeue()
            
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            
        return traversal


    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return re.sub('-$','',self.preorder_search(tree.root, ""))
        
        elif traversal_type == "inorder":
            return re.sub('-$','',self.inorder_search(tree.root, ""))
        
        elif traversal_type == "postorder":
            return re.sub('-$','',self.postorder_search(tree.root, ""))
        
        elif traversal_type == "BFS":
            return re.sub('-$','',self.Breadth_first_search(tree.root))

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False



# Construct a binary tree
'''
     1
    / \
   2   3
  / \
 4   5
  
'''

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.left = Node(6)


print("Breadth first search:")
print(tree.print_tree("BFS"))

print("preorder search:") 
print(tree.print_tree("preorder"))

print("inorder search:") 
print(tree.print_tree("inorder"))
    
print("postorder search:") 
print(tree.print_tree("postorder"))
    