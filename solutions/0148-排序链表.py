# Problem Id:  148
# Problem Name:  Sort List, 排序链表
# Problem Url:  https://leetcode-cn.com/problems/sort-list/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        else:
            slow = head
            fast = head
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            right = self.sortList(slow.next)
            slow.next = None
            left = self.sortList(head)
            return self.mergeList(left,right)

    def mergeList(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        node = res
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
                node = node.next
            else:
                node.next = l2
                l2 = l2.next
                node = node.next
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        return res.next
