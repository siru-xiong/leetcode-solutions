# Problem Id:  426
# Problem Name:  Convert Binary Search Tree to Sorted Doubly Linked List, 将二叉搜索树转化为排序的双向链表
# Problem Url:  https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# Problem Level:  Medium
 
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        elif not root.left and not root.right:
            root.left = root
            root.right = root
            return root
        else:
            l = self.treeToDoublyList(root.left)
            r = self.treeToDoublyList(root.right)
            q = l
            if q:
                while q.val < q.right.val:
                    q = q.right
                q.right = Node(val=root.val)
                q.right.left = q
                q = q.right
                q.right = r
            else:
                q = Node(val=root.val)
                q.right = r
                l = q
            if r:
                q.right.left = q
                while q.val < q.right.val:
                    q = q.right
            q.right = l
            l.left = q
            return l
