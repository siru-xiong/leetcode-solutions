# Problem Id:  82
# Problem Name:  Remove Duplicates from Sorted List II, 删除排序链表中的重复元素 II
# Problem Url:  https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = ListNode()
        q = p
        while head:
            i = 0
            while head.next and head.next.val == head.val:
                head = head.next
                i = i + 1
            if i == 0:
                q.next = head
                head = head.next
                q = q.next
                q.next = None
            else:
                head = head.next
        return p.next