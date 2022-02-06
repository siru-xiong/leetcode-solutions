# Problem Id:  剑指 Offer 26
# Problem Name:  树的子结构  LCOF, 树的子结构
# Problem Url:  https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isstrict(self,A,B):
        if not A and not B:
            return True
        elif not A and B:
            return False
        elif not B and A:
            return True
        else:
            if A.val == B.val:
                return self.isstrict(A.left,B.left) and self.isstrict(A.right,B.right)
            else:
                return False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not A and not B:
            return False
        elif not A and B:
            return False
        elif A and not B:
            return False
        else:
            res = False
            if A.val == B.val:
                res = res or self.isstrict(A,B)
            res = res or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B)
            return res