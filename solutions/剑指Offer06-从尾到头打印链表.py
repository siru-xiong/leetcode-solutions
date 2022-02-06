# Problem Id:  剑指 Offer 06
# Problem Name:  从尾到头打印链表 LCOF, 从尾到头打印链表
# Problem Url:  https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        elif not head.next:
            return [head.val]
        else:
            return self.reversePrint(head.next) + [head.val]