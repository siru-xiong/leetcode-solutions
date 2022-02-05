# Problem Id:  109
# Problem Name:  Convert Sorted List to Binary Search Tree, 有序链表转换二叉搜索树
# Problem Url:  https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/
# Problem Level:  Medium
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        elif not head.next:
            return TreeNode(val=head.val)
        else:
            a = head
            b = head
            b = b.next.next
            while b and b.next:
                a = a.next
                b = b.next.next
            vl = a.next.val
            right = self.sortedListToBST(a.next.next)
            a.next = None
            left = self.sortedListToBST(head)
            return TreeNode(val=vl,left=left,right=right)