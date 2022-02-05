# Problem Id:  102
# Problem Name:  Binary Tree Level Order Traversal, 二叉树的层序遍历
# Problem Url:  https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        else:
            t = [[root.val]]
            left = self.levelOrder(root.left)
            right = self.levelOrder(root.right)
            for i in range(len(right)):
                if i >= len(left):
                    left.append([])
                left[i].extend(right[i])
            t = t + left
            return t