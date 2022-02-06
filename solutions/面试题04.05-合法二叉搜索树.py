# Problem Id:  面试题 04.05
# Problem Name:  Legal Binary Search Tree LCCI, 合法二叉搜索树
# Problem Url:  https://leetcode-cn.com/problems/legal-binary-search-tree-lcci/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(rt,mi=float('-inf'),ma=float('inf')):
            if not rt:
                return True
            else:
                if rt.val < ma and rt.val > mi:
                    return dfs(rt.left,mi,rt.val) and dfs(rt.right,rt.val,ma)
                else:
                    return False
        return dfs(root)