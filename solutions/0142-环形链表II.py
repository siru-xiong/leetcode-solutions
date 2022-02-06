# Problem Id:  142
# Problem Name:  Linked List Cycle II, 环形链表 II
# Problem Url:  https://leetcode-cn.com/problems/linked-list-cycle-ii/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        while fast:
            slow = slow.next
            if not fast.next:
                return None
            fast = fast.next.next
            if fast == slow:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None
