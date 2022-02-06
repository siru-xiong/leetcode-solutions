# Problem Id:  559
# Problem Name:  Maximum Depth of N-ary Tree, N 叉树的最大深度
# Problem Url:  https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/
# Problem Level:  Easy
# Language:  Python3
 
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        elif len(root.children) == 0:
            return 1
        else:
            return 1 + max([self.maxDepth(i) for i in root.children])