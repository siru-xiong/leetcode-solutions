# Problem Id:  2
# Problem Name:  Add Two Numbers, 两数相加
# Problem Url:  https://leetcode-cn.com/problems/add-two-numbers/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        r = res
        index = 0
        while l1 and l2:
            temp = l1.val + l2.val
            if temp+index >= 10:
                r.next = ListNode(val=(temp+index)%10)
                index = 1
                r = r.next
                l1 = l1.next
                l2 = l2.next
            else:
                r.next = ListNode(val=temp+index)
                index = 0
                r = r.next
                l1 = l1.next
                l2 = l2.next
        for i in (l1,l2):
            while i:
                temp = i.val + index
                if temp >= 10:
                    r.next = ListNode(val=temp%10)
                    index = 1
                    r = r.next
                    i = i.next
                else:
                    r.next = ListNode(val=temp)
                    index = 0
                    r = r.next
                    i = i.next
        if index == 1:
            r.next = ListNode(1)
        return res.next
