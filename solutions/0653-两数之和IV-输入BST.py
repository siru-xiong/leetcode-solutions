# Problem Id:  653
# Problem Name:  Two Sum IV - Input is a BST, 两数之和 IV - 输入 BST
# Problem Url:  https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        res = []
        def dfs(root):
            if not root:
                pass
            else:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
        dfs(root)
        i = 0
        j = len(res)-1
        result = False
        while j>i:
            if res[i] + res[j] > k:
                j = j -1
            elif res[i] + res[j] < k:
                i = i + 1
            else:
                result = True
                break
        return result
            