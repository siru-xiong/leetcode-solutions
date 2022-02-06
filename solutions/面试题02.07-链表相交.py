# Problem Id:  面试题 02.07
# Problem Name:  Intersection of Two Linked Lists LCCI, 链表相交
# Problem Url:  https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        else:
            seta = set()
            while headA:
                seta.add(headA)
                headA = headA.next
            result = 0
            while headB:
                if headB in seta:
                    result = 1
                    return headB
                    break
                else:
                    headB = headB.next
            if result == 0:
                return None