# Problem Id:  328
# Problem Name:  Odd Even Linked List, 奇偶链表
# Problem Url:  https://leetcode-cn.com/problems/odd-even-linked-list/
# Problem Level:  Medium
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        evenhead = head.next
        odd = head
        even = evenhead
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head