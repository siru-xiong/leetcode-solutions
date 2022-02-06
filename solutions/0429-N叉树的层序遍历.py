# Problem Id:  429
# Problem Name:  N-ary Tree Level Order Traversal, N 叉树的层序遍历
# Problem Url:  https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
# Problem Level:  Medium
# Language:  Python3
 
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        def dfs(r,i):
            if not r:
                pass
            else:
                while len(res) < i:
                    res.append([])
                res[i-1].append(r.val)
                for j in r.children:
                    dfs(j,i+1)
        dfs(root,1)
        return res