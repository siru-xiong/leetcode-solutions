# Problem Id:  面试题 02.01
# Problem Name:  Remove Duplicate Node LCCI, 移除重复节点
# Problem Url:  https://leetcode-cn.com/problems/remove-duplicate-node-lcci/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        c = set()
        node = head
        while node:
            c.add(node.val)
            node = node.next
        res = ListNode(head.val)
        out = res
        c.remove(head.val)
        head = head.next
        while head:
            if head.val in c:
                t = ListNode(head.val)
                out.next = t
                out = out.next
                c.remove(head.val)
                head = head.next
            else:
                head = head.next
        return res

