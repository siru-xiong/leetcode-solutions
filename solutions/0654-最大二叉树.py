# Problem Id:  654
# Problem Name:  Maximum Binary Tree, 最大二叉树
# Problem Url:  https://leetcode-cn.com/problems/maximum-binary-tree/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nl: List[int]) -> TreeNode:
        if len(nl) == 0:
            return None
        elif len(nl) == 1:
            return TreeNode(val=nl[0])
        elif len(nl) == 2:
            if nl[0] > nl[1]:
                return TreeNode(val=nl[0],right=TreeNode(val=nl[1]))
            else:
                return TreeNode(val=nl[1],left=TreeNode(val=nl[0]))
        else:
            vm = max(nl)
            for i in range(len(nl)):
                if nl[i] == vm:
                    tp = i
                    break
            tl = self.constructMaximumBinaryTree(nl[:i])
            tr = self.constructMaximumBinaryTree(nl[(i+1):])
            return TreeNode(val=nl[i],left=tl,right=tr)
