# Problem Id:  993
# Problem Name:  Cousins in Binary Tree, 二叉树的堂兄弟节点
# Problem Url:  https://leetcode-cn.com/problems/cousins-in-binary-tree/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, root , t, index):
        if not root or (not root.left and not root.right):
            return -1
        elif not root.right:
            if root.left.val == t:
                return [root.val,index+1]
            else:
                return self.find(root.left,t,index+1)
        elif not root.left:
            if root.right.val == t:
                return [root.val,index+1]
            else:
                return self.find(root.right,t,index+1)
        else:
            if root.left.val == t or root.right.val == t:
                return [root.val,index+1]
            else:
                r = self.find(root.right,t,index+1)
                l = self.find(root.left,t,index+1)
                if r != -1:
                    return r
                elif l != -1:
                    return l
                else:
                    return -1
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        elif root.val in [x,y]:
            return False
        else:
            a = self.find(root,x,1)
            b = self.find(root,y,1)
            return a != -1 and b!= -1 and a[0] != b[0] and a[1] == b[1]