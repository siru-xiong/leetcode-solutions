# Problem Id:  61
# Problem Name:  Rotate List, 旋转链表
# Problem Url:  https://leetcode-cn.com/problems/rotate-list/
# Problem Level:  Medium
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        elif k == 0:
            return head
        else:
            leng = 0
            node = head
            while node:
                leng += 1
                node = node.next
            k = k % leng
            if k == 0:
                return head
            node = head
            left = leng - k
            while left > 1:
                node = node.next
                left -= 1
            t = node.next
            node.next = None
            x = t
            while x.next:
                x = x.next
            x.next = head
            return t
            
