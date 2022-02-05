# Problem Id:  513
# Problem Name:  Find Bottom Left Tree Value, 找树左下角的值
# Problem Url:  https://leetcode-cn.com/problems/find-bottom-left-tree-value/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def d(self,root:TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.d(root.left) , self.d(root.right))
    
    def s(self,root:TreeNode,d:int) -> int:
        if not root:
            return None
        elif d == 1:
            return root.val
        else:
            a = self.s(root.left,d-1)
            if a != None:
                return a
            else:
                return self.s(root.right,d-1)

    def findBottomLeftValue(self, root: TreeNode) -> int:
        return self.s(root,self.d(root))
        

            