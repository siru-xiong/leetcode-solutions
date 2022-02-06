# Problem Id:  113
# Problem Name:  Path Sum II, 路径总和 II
# Problem Url:  https://leetcode-cn.com/problems/path-sum-ii/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root:
            if target == 0:
                return []
            else:
                return []
        elif not root.left and not root.right:
            if target == root.val:
                return [[root.val]]
            else:
                return []
        else:
            a = self.pathSum(root.left,target-root.val)
            b = self.pathSum(root.right,target-root.val)
            res = []
            if len(a) > 0:
                res = res + [[root.val]+i for i in a]
            if len(b) > 0:
                res = res + [[root.val]+i for i in b]
            return res