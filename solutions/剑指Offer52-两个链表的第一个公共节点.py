# Problem Id:  剑指 Offer 52
# Problem Name:  两个链表的第一个公共节点  LCOF, 两个链表的第一个公共节点
# Problem Url:  https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
# Problem Level:  Easy
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seta = set()
        while headA:
            seta.add(headA)
            headA = headA.next
        while headB:
            if headB in seta:
                return headB
            else:
                headB = headB.next
        return None