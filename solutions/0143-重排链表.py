# Problem Id:  143
# Problem Name:  Reorder List, 重排链表
# Problem Url:  https://leetcode-cn.com/problems/reorder-list/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
    
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        res = head
        while res:
            count = count + 1
            res = res.next
        count = int(count / 2)
        while count >= 1:
            head = head.next
            count = count - 1
        return head
    
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

    def mergeList(self, l1: ListNode, l2: ListNode):
        p = l1
        q = l2
        while p and q:
            n = p.next
            p.next = q
            m = q.next
            p = p.next
            p.next = n
            p = p.next
            q = m