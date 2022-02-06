# Problem Id:  面试题 02.03
# Problem Name:  Delete Middle Node LCCI, 删除中间节点
# Problem Url:  https://leetcode-cn.com/problems/delete-middle-node-lcci/
# Problem Level:  Easy
# Language:  Python3
 
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
        t = node
        while t.next:
            t.val = t.next.val
            if not t.next.next:
                t.next = None
                break
            t = t.next
            
        