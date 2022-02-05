# Problem Id:  897
# Problem Name:  Increasing Order Search Tree, 递增顺序搜索树
# Problem Url:  https://leetcode-cn.com/problems/increasing-order-search-tree/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        vals = []
        def dfs(node):
            if node != None:
                dfs(node.left)
                vals.append(node.val)
                dfs(node.right)
        dfs(root)
        result = TreeNode(val = vals[-1])
        for i in range(2,len(vals)+1):
            result = TreeNode(val=vals[-i],right=result)
        return result