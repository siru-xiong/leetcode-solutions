# Problem Id:  98
# Problem Name:  Validate Binary Search Tree, 验证二叉搜索树
# Problem Url:  https://leetcode-cn.com/problems/validate-binary-search-tree/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        save = []
        def dfs(root):
            if not root:
                pass
            else:
                dfs(root.left)
                save.append(root.val)
                dfs(root.right)
        dfs(root)
        result = True
        if len(save) == 0:
            return True
        else:
            for i in range(1,len(save)):
                if save[i-1] >= save[i]:
                    result = False
                    break
            return result
        