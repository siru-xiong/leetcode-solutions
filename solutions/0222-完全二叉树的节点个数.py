# Problem Id:  222
# Problem Name:  Count Complete Tree Nodes, 完全二叉树的节点个数
# Problem Url:  https://leetcode-cn.com/problems/count-complete-tree-nodes/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = 0        
        def de(root):
            if not root:
                return 0
            else:
                return 1 + max(de(root.left),de(root.right))
        d = de(root)
        def cd(root,r):
            if r == 1:
                if root:
                    return 1
                else:
                    return 0
            else:
                return cd(root.left,r-1)+cd(root.right,r-1)
        s = cd(root,d)
        res = 0
        i = 1
        t = 1
        while t < d:
            res = res + i
            i *= 2
            t = t + 1
        res = res + s
        return res

            