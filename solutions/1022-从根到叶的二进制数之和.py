# Problem Id:  1022
# Problem Name:  Sum of Root To Leaf Binary Numbers, 从根到叶的二进制数之和
# Problem Url:  https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return []
            else:
                if not root.left and not root.right:
                    return [[root.val]]
                elif not root.left:
                    return [[root.val]+i for i in dfs(root.right)]
                elif not root.right:
                    return [[root.val]+i for i in dfs(root.left)]
                else:
                    return [[root.val]+i for i in dfs(root.left)]+[[root.val]+i for i in dfs(root.right)]
        res = dfs(root)
        count = 0
        for i in range(len(res)):
            index = 1
            for j in range(1,len(res[i])+1):
                count = count + res[i][-j]*index
                index = index * 2
        return count
