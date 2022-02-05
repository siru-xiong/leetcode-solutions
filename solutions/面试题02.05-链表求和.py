# Problem Id:  面试题 02.05
# Problem Name:  Sum Lists LCCI, 链表求和
# Problem Url:  https://leetcode-cn.com/problems/sum-lists-lcci/
# Problem Level:  Medium
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        index = 0
        res = ListNode(0)
        t = res
        while l1 or l2:
            if not l1:
                a = 0
            else:
                a = l1.val
                l1 = l1.next
            
            if not l2:
                b = 0
            else:
                b = l2.val
                l2 = l2.next
        
            if index == 0:
                n = a + b
            else:
                n = a + b + 1
            
            if n >= 10:
                index = 1
                n = n % 10
            else:
                index = 0
            
            r = ListNode(n)
            t.next = r
            t = t.next
        
        if index == 1:
            r = ListNode(1)
            t.next = r
        
        return res.next