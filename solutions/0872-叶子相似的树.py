# Problem Id:  872
# Problem Name:  Leaf-Similar Trees, 叶子相似的树
# Problem Url:  https://leetcode-cn.com/problems/leaf-similar-trees/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fl(self, root : TreeNode):
        if not root.left and not root.right:
            return [root.val]
        elif not root.left:
            return self.fl(root.right)
        elif not root.right:
            return self.fl(root.left)
        else:
            return self.fl(root.left)+self.fl(root.right)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.fl(root1) == self.fl(root2)

        
