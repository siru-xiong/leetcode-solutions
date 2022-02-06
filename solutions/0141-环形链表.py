# Problem Id:  141
# Problem Name:  Linked List Cycle, 环形链表
# Problem Url:  https://leetcode-cn.com/problems/linked-list-cycle/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        value = set()
        result = False
        while head:
            if head not in value:
                value.add(head)
                head = head.next
            else:
                result = True
                break
        return result