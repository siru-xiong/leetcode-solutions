# Problem Id:  面试题 02.06
# Problem Name:  Palindrome Linked List LCCI, 回文链表
# Problem Url:  https://leetcode-cn.com/problems/palindrome-linked-list-lcci/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        node = head
        while node:
            res.append(node.val)
            node = node.next
        if len(res) == 0:
            return True
        l = 0
        r = len(res)-1
        while l <= r:
            if res[l] == res[r]:
                l += 1
                r -= 1
            else:
                return False
        return True