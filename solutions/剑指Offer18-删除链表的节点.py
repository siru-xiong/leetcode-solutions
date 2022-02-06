# Problem Id:  剑指 Offer 18
# Problem Name:  删除链表的节点 LCOF, 删除链表的节点
# Problem Url:  https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        node = head
        if node.val == val:
            return node.next
        else:
            while node.next.val != val:
                node = node.next
        
            r = node.next.next
            node.next = r
            return head
