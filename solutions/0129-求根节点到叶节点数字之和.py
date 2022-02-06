# Problem Id:  129
# Problem Name:  Sum Root to Leaf Numbers, 求根节点到叶节点数字之和
# Problem Url:  https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumlist(self, root):
        if not root:
            return []
        elif not root.left and not root.right:
            return [str(root.val)]
        else:
            left = [str(root.val)+i for i in self.sumlist(root.left)]
            right = [str(root.val)+i for i in self.sumlist(root.right)]
            return left+right

    def sumNumbers(self, root: TreeNode) -> int:
        return sum([int(x) for x in self.sumlist(root)])
