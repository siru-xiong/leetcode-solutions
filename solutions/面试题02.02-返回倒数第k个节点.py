# Problem Id:  面试题 02.02
# Problem Name:  Kth Node From End of List LCCI, 返回倒数第 k 个节点
# Problem Url:  https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        a = head
        b = head
        for i in range(k-1):
            b = b.next
        while b.next:
            a = a.next
            b = b.next
        return a.val