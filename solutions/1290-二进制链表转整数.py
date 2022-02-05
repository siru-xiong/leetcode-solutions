# Problem Id:  1290
# Problem Name:  Convert Binary Number in a Linked List to Integer, 二进制链表转整数
# Problem Url:  https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Problem Level:  Easy
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count = 0
        res = head
        while res:
            count = count + 1
            res = res.next
        index = pow(2,count-1)
        result = 0
        while head:
            result = result + head.val * index
            index = index / 2
            head = head.next
        return int(result)