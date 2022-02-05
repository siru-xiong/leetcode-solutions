# Problem Id:  237
# Problem Name:  Delete Node in a Linked List, 删除链表中的节点
# Problem Url:  https://leetcode-cn.com/problems/delete-node-in-a-linked-list/
# Problem Level:  Easy
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next