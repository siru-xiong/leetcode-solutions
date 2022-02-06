# Problem Id:  671
# Problem Name:  Second Minimum Node In a Binary Tree, 二叉树中第二小的节点
# Problem Url:  https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = [float('inf'),float('inf')]
        def dfs(root):
            if not root:
                pass
            else:
                if root.val < res[0]:
                    res[0],res[1] = root.val,res[0]
                elif root.val < res[1] and root.val != res[0]:
                    res[1] = root.val
                if not root.left:
                    pass
                else:
                    dfs(root.left)
                    dfs(root.right)
        dfs(root)
        if res[1] != float('inf'):
            return res[1]
        else:
            return -1

            