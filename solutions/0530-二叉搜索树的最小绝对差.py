# Problem Id:  530
# Problem Name:  Minimum Absolute Difference in BST, 二叉搜索树的最小绝对差
# Problem Url:  https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = []
        def dfs(root):
            if not root:
                pass
            else:
                res.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        res.sort()
        vmin = float('inf')
        for i in range(1,len(res)):
            if abs(res[i]-res[i-1]) < vmin:
                vmin = res[i] - res[i-1]
        return vmin