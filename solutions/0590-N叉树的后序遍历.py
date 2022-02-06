# Problem Id:  590
# Problem Name:  N-ary Tree Postorder Traversal, N 叉树的后序遍历
# Problem Url:  https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
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
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        def po(root: 'Node'):
            if not po:
                pass
            else:
                for i in root.children:
                    po(i)
                res.append(root.val)
        po(root)
        return res