# Problem Id:  剑指 Offer 24
# Problem Name:  反转链表 LCOF, 反转链表
# Problem Url:  https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        res = None
        if not head:
            return head
        while head:
            t = ListNode(head.val)
            t.next = res
            res = t
            head = head.next
        return t