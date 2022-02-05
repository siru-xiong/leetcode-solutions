# Problem Id:  116
# Problem Name:  Populating Next Right Pointers in Each Node, 填充每个节点的下一个右侧节点指针
# Problem Url:  https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
# Problem Level:  Medium
 
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def fit(self,l,r):
        if not l or not r:
            return (l,r)
        else:
            l.next = r
            if l.right:
                l.right,r.left = self.fit(l.right,r.left)
            return (l,r)

    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left and not root.right:
            return root
        else:
            root.left = self.connect(root.left)
            root.right = self.connect(root.right)
            root.left, root.right = self.fit(root.left,root.right)
            return root