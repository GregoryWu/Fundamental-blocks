# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 11:37:51 2020

@author: popeg
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head # connect with the head
    first = head
    length = 0
    while first is not None:
        first = first.next
        length += 1
    
    length -= n
    first = dummy

    while length > 0:
        first = first.next
        length -= 1
    first.next = first.next.next # skip the nth element from the end
    
    return dummy.next

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)


removeNthFromEnd(a,2)


