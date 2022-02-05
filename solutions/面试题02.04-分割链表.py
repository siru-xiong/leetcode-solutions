# Problem Id:  面试题 02.04
# Problem Name:  Partition List LCCI, 分割链表
# Problem Url:  https://leetcode-cn.com/problems/partition-list-lcci/
# Problem Level:  Medium
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        res = ListNode(0)
        t = res
        node = head
        while node:
            if node.val < x:
                t.next = ListNode(node.val)
                t = t.next
            node = node.next
        node = head
        while node:
            if node.val >= x:
                t.next = ListNode(node.val)
                t = t.next
            node = node.next
        return res.next