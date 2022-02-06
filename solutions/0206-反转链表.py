# Problem Id:  206
# Problem Name:  Reverse Linked List, 反转链表
# Problem Url:  https://leetcode-cn.com/problems/reverse-linked-list/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if  head == None:
            return None
        elif  head.next == None:
            return head
        else:
            result = self.reverseList(head.next)
            node = result
            while node.next != None:
                node = node.next
            node.next = ListNode(val=head.val)
            return result