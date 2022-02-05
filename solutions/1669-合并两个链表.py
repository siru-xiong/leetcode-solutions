# Problem Id:  1669
# Problem Name:  Merge In Between Linked Lists, 合并两个链表
# Problem Url:  https://leetcode-cn.com/problems/merge-in-between-linked-lists/
# Problem Level:  Medium
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        root = list1
        for i in range(a-1):
            root = root.next
        p1 = root.next
        root.next = list2
        
        for i in range(b-a+1):
            p1 = p1.next
        
        while root.next:
            root = root.next
        root.next = p1

        return list1