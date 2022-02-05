# Problem Id:  86
# Problem Name:  Partition List, 分隔链表
# Problem Url:  https://leetcode-cn.com/problems/partition-list/
# Problem Level:  Medium
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode()
        large = ListNode()
        p = small
        q = large
        while head:
            if head.val < x:
                p.next = ListNode(val=head.val)
                p = p.next
            else:
                q.next = ListNode(val=head.val)
                q = q.next
            head = head.next
        p.next = large.next
        return small.next