# Problem Id:  1008
# Problem Name:  Construct Binary Search Tree from Preorder Traversal, 前序遍历构造二叉搜索树
# Problem Url:  https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        elif len(preorder) == 1:
            return TreeNode(val=preorder[0])
        else:
            v = preorder[0]
            t = len(preorder)
            for i in range(len(preorder)):
                if preorder[i] > v:
                    t = i
                    break
            l = self.bstFromPreorder(preorder[1:t])
            r = self.bstFromPreorder(preorder[t:])
            return TreeNode(v,l,r)