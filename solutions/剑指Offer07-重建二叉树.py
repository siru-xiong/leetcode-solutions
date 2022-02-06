# Problem Id:  剑指 Offer 07
# Problem Name:  重建二叉树 LCOF, 重建二叉树
# Problem Url:  https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        elif len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])
        else:
            res = TreeNode(preorder[0])
            for i in range(len(inorder)):
                if inorder[i] == preorder[0]:
                    index = i
                    break
            res.left = self.buildTree(preorder[1:(1+index)],inorder[:index])
            res.right = self.buildTree(preorder[(1+index):],inorder[(index+1):])
            return res