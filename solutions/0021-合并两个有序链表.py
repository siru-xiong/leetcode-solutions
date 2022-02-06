# Problem Id:  21
# Problem Name:  Merge Two Sorted Lists, 合并两个有序链表
# Problem Url:  https://leetcode-cn.com/problems/merge-two-sorted-lists/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(val = 0)
        node = res
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
                node = node.next
            else:
                node.next = l2
                l2 = l2.next
                node = node.next
        while l1:
            node.next = l1
            l1 = l1.next
            node = node.next
            node.next = None
        while l2:
            node.next = l2
            l2 = l2.next
            node = node.next
            node.next = None
        return res.next
