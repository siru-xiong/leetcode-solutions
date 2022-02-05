# Problem Id:  面试题 17.12
# Problem Name:  BiNode LCCI, BiNode
# Problem Url:  https://leetcode-cn.com/problems/binode-lcci/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            res = self.convertBiNode(root.left)
            if not res:
                res = TreeNode(root.val)
                res.right = self.convertBiNode(root.right)
                return res
            else:
                node = res
                while node.right:
                    node = node.right
                node.right = TreeNode(root.val)
                node = node.right
                node.right = self.convertBiNode(root.right)
                return res