# Problem Id:  25
# Problem Name:  Reverse Nodes in k-Group, K 个一组翻转链表
# Problem Url:  https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
# Problem Level:  Hard
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head) -> ListNode:
        if not head:
            return None
        elif not head.next:
            return head
        else:
            a = self.reverse(head.next)
            head.next = None
            b = a
            while b.next:
                b = b.next
            b.next = head
            return a


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        else:
            i = 0 
            p = head
            while i < k-1:
                if not p:
                    return head
                p = p.next
                i = i + 1
            if not p:
                return head
            t = p.next
            p.next = None
            f = self.reverse(head)
            g = self.reverseKGroup(t,k)
            l = f
            while l.next:
                l = l.next
            l.next = g
            return f