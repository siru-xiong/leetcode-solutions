# Problem Id:  1490
# Problem Name:  Clone N-ary Tree, 克隆 N 叉树
# Problem Url:  https://leetcode-cn.com/problems/clone-n-ary-tree/
# Problem Level:  Medium
 
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        if root.children is None:
            return Node(val=self.val,children = [])
        else:
            r = []
            for i in root.children:
                r.append(self.cloneTree(i))
            return Node(val=root.val,children=r)