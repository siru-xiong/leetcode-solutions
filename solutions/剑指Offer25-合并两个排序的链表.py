# Problem Id:  剑指 Offer 25
# Problem Name:  合并两个排序的链表  LCOF, 合并两个排序的链表
# Problem Url:  https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
# Problem Level:  Easy
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
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
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        return res.next