# Problem Id:  1379
# Problem Name:  Find a Corresponding Node of a Binary Tree in a Clone of That Tree, 找出克隆二叉树中的相同节点
# Problem Url:  https://leetcode-cn.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        elif original == target:
            return cloned
        else:
            left = self.getTargetCopy(original.left, cloned.left, target)
            if left:
                return left
            else:
                return self.getTargetCopy(original.right, cloned.right, target)