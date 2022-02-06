# Problem Id:  589
# Problem Name:  N-ary Tree Preorder Traversal, N 叉树的前序遍历
# Problem Url:  https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
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
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(r):
            if not r:
                pass
            else:
                res.append(r.val)
                for i in r.children:
                    dfs(i)
        dfs(root)
        return res