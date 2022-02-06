# Problem Id:  面试题 02.08
# Problem Name:  Linked List Cycle LCCI, 环路检测
# Problem Url:  https://leetcode-cn.com/problems/linked-list-cycle-lcci/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        c = 0
        nc = 0
        while True:
            if not fast or not fast.next:
                nc = 1
                break
            else:
                fast = fast.next.next
                slow = slow.next
            if fast == slow:
                c = 1
                break
        
        if nc == 1:
            return None
        else:
            node = head
            while node != slow:
                node = node.next
                slow = slow.next
            return slow
        