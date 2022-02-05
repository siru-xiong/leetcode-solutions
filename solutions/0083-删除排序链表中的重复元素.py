# Problem Id:  83
# Problem Name:  Remove Duplicates from Sorted List, 删除排序链表中的重复元素
# Problem Url:  https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
# Problem Level:  Easy
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        result = ListNode(None)
        node = result
        save = set()
        while head:
            if head.val not in save:
                save.add(head.val)
                node.next = head
                head = head.next
                node = node.next
                node.next = None
            else:
                head = head.next

        return result.next