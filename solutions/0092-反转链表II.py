# Problem Id:  92
# Problem Name:  Reverse Linked List II, 反转链表 II
# Problem Url:  https://leetcode-cn.com/problems/reverse-linked-list-ii/
# Problem Level:  Medium
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

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next:
            return head
        head = ListNode(val = 0,next=head)
        start = head
        i = 1
        while i != left:
            start = start.next
            i = i + 1
        end = start
        while i != right + 1:
            end = end.next
            i = i + 1
        r = end.next
        end.next = None
        start.next = self.reverseList(start.next)
        q = start
        while q.next:
            q = q.next
        q.next = r
        return head.next