# Problem Id:  606
# Problem Name:  Construct String from Binary Tree, 根据二叉树创建字符串
# Problem Url:  https://leetcode-cn.com/problems/construct-string-from-binary-tree/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        s = []
        def myfun(t: TreeNode):
            if not t:
                pass
            elif not t.left and not t.right:
                s.append(str(t.val))
            else:
                s.append(str(t.val))
                s.append('(')
                myfun(t.left)
                s.append(')')
                if t.right:
                    s.append('(')
                    myfun(t.right)
                    s.append(')')
        myfun(t)
        return ''.join(s)
