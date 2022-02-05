# Problem Id:  剑指 Offer 36
# Problem Name:  二叉搜索树与双向链表  LCOF, 二叉搜索树与双向链表
# Problem Url:  https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
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
