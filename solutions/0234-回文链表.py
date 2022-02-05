# Problem Id:  234
# Problem Name:  Palindrome Linked List, 回文链表
# Problem Url:  https://leetcode-cn.com/problems/palindrome-linked-list/
# Problem Level:  Easy
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num = []
        while head:
            num.append(head.val)
            head = head.next
        return num == num[::-1]