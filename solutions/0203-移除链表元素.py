# Problem Id:  203
# Problem Name:  Remove Linked List Elements, 移除链表元素
# Problem Url:  https://leetcode-cn.com/problems/remove-linked-list-elements/
# Problem Level:  Easy
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        result = ListNode(None)
        node = result
        while head:
            if head.val != val:
                node.next = head
                head = head.next
                node = node.next
                node.next = None
            else:
                head = head.next
        return result.next