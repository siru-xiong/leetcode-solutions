# Problem Id:  24
# Problem Name:  Swap Nodes in Pairs, 两两交换链表中的节点
# Problem Url:  https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        else:
            tail = head.next
            head.next = self.swapPairs(head.next.next)
            tail.next = head
            return tail