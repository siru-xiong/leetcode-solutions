# Problem Id:  117
# Problem Name:  Populating Next Right Pointers in Each Node II, 填充每个节点的下一个右侧节点指针 II
# Problem Url:  https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
# Problem Level:  Medium
# Language:  Python3
 
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
            l.right,r.right = self.fit(l.right,r.right)
            l.right,r.left = self.fit(l.right,r.left)
            l.left,r.right = self.fit(l.left,r.right)
            l.left,r.left = self.fit(l.left,r.left)
            return (l,r)

    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left and not root.right:
            return root
        else:
            root.left, root.right = self.fit(root.left,root.right)
            root.left = self.connect(root.left)
            root.right = self.connect(root.right)
            return root