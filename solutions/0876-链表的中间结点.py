# Problem Id:  876
# Problem Name:  Middle of the Linked List, 链表的中间结点
# Problem Url:  https://leetcode-cn.com/problems/middle-of-the-linked-list/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        res = head
        while res:
            count = count + 1
            res = res.next
        count = int(count / 2)
        while count >= 1:
            head = head.next
            count = count - 1
        return head
        
