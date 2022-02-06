# Problem Id:  1302
# Problem Name:  Deepest Leaves Sum, 层数最深叶子节点的和
# Problem Url:  https://leetcode-cn.com/problems/deepest-leaves-sum/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def depth(r):
            if not r:
                return 0
            else:
                return 1 + max(depth(r.left),depth(r.right))
        d = depth(root)

        def fetch(r,t):
            if t == 1:
                if not r:
                    return 0
                else:
                    return r.val
            elif not r:
                return 0
            else:
                return fetch(r.left,t-1) + fetch(r.right,t-1)
        return fetch(root,d)