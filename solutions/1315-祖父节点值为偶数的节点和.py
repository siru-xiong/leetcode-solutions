# Problem Id:  1315
# Problem Name:  Sum of Nodes with Even-Valued Grandparent, 祖父节点值为偶数的节点和
# Problem Url:  https://leetcode-cn.com/problems/sum-of-nodes-with-even-valued-grandparent/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode, top = False) -> int:
        if not root:
            return 0
        elif top == False and root.val % 2 != 0:
            return self.sumEvenGrandparent(root.left,False)+self.sumEvenGrandparent(root.right,False)
        elif top == False and root.val % 2 == 0:
            return self.sumEvenGrandparent(root.left,True)+self.sumEvenGrandparent(root.right,True)
        else:
            t = 0
            if root.left:
                t += root.left.val
            if root.right:
                t += root.right.val
            if root.val % 2 == 0:
                return t + self.sumEvenGrandparent(root.left,True)+self.sumEvenGrandparent(root.right,True)
            else:
                return t + self.sumEvenGrandparent(root.left,False)+self.sumEvenGrandparent(root.right,False)