# Problem Id:  437
# Problem Name:  Path Sum III, 路径总和 III
# Problem Url:  https://leetcode-cn.com/problems/path-sum-iii/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        self.dfs(root,targetSum)
        self.pathSum(root.left,targetSum)
        self.pathSum(root.right,targetSum)
        return self.count

    def dfs(self,root,s):
        if not root:
            pass
        else:
            s = s - root.val
            if s == 0:
                self.count += 1
            self.dfs(root.left,s)
            self.dfs(root.right,s)