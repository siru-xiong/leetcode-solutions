# Problem Id:  面试题 04.10
# Problem Name:  Check SubTree LCCI, 检查子树
# Problem Url:  https://leetcode-cn.com/problems/check-subtree-lcci/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t2:
            return True
        elif not t1:
            return False
        else:
            return self.eq(t1,t2) or self.checkSubTree(t1.left,t2) or self.checkSubTree(t1.right,t2)
    
    def eq(self, t1:TreeNode,t2:TreeNode) -> bool:
        if not t1 and not t2:
            return True
        elif t1 and t2:
            return t1.val == t2.val and self.eq(t1.left,t2.left) and self.eq(t1.right,t2.right)
        else:
            return False
