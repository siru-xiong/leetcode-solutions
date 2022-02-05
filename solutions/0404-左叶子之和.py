# Problem Id:  404
# Problem Name:  Sum of Left Leaves, 左叶子之和
# Problem Url:  https://leetcode-cn.com/problems/sum-of-left-leaves/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 0
        elif not root.left:
            return self.sumOfLeftLeaves(root.right)
        elif not root.right:
            if not root.left.left and not root.left.right:
                return root.left.val
            else:
                return self.sumOfLeftLeaves(root.left)
        else:
            if not root.left.left and not root.left.right:
                return root.left.val+self.sumOfLeftLeaves(root.right)
            else:
                return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)