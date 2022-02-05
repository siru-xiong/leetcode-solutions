# Problem Id:  270
# Problem Name:  Closest Binary Search Tree Value, 最接近的二叉搜索树值
# Problem Url:  https://leetcode-cn.com/problems/closest-binary-search-tree-value/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root.left and not root.right:
            return root.val
        else:
            if target == root.val:
                return root.val
            elif target > root.val:
                if not root.right:
                    return root.val
                else:
                    res = self.closestValue(root.right,target)
                    if abs(res - target) < abs(root.val - target):
                        return res
                    else:
                        return root.val
            else:
                if not root.left:
                    return root.val
                else:
                    res = self.closestValue(root.left,target)
                    if abs(res - target) < abs(root.val - target):
                        return res
                    else:
                        return root.val