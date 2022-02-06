# Problem Id:  430
# Problem Name:  Flatten a Multilevel Doubly Linked List, 扁平化多级双向链表
# Problem Url:  https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/
# Problem Level:  Medium
# Language:  Python3
 
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        elif not head.child:
            head.next = self.flatten(head.next)
            return head
        else:
            c = self.flatten(head.child)
            n = self.flatten(head.next)
            head.child = None
            head.next = None
            p = head
            if c:
                c.prev = None
                p.next = c
                p.next.prev = p
                q = p
                while q.next:
                    q = q.next
            else:
                q = head
            if n:
                n.prev = None
                q.next = n
                q.next.prev = q
            return head
            