# Problem Id:  1305
# Problem Name:  All Elements in Two Binary Search Trees, 两棵二叉搜索树中的所有元素
# Problem Url:  https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def ge(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return self.ge(root.left) + [root.val] + self.ge(root.right)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        x = self.ge(root1)
        y = self.ge(root2)
        i = 0
        j = 0
        res = []
        while i < len(x) and j < len(y):
            if x[i] <= y[j]:
                res.append(x[i])
                i = i + 1
            else:
                res.append(y[j])
                j = j + 1
        if i < len(x):
            res = res + x[i:]
        if j < len(y):
            res = res + y[j:]
        return res
