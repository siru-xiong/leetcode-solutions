# Problem Id:  剑指 Offer II 054
# Problem Name:  所有大于等于节点的值之和, 所有大于等于节点的值之和
# Problem Url:  https://leetcode-cn.com/problems/w6cpku/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)
        total = 0
        dfs(root)
        return root