# Problem Id:  剑指 Offer 22
# Problem Name:  链表中倒数第k个节点 LCOF, 链表中倒数第k个节点
# Problem Url:  https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        n = 0
        node = head
        while node:
            n = n + 1
            node = node.next
        n = n - k
        while n > 0:
            head = head.next
            n -= 1
        return head
            