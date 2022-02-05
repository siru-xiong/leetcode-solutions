# Problem Id:  1325
# Problem Name:  Delete Leaves With a Given Value, 删除给定值的叶子节点
# Problem Url:  https://leetcode-cn.com/problems/delete-leaves-with-a-given-value/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None
        elif not root.left and not root.right:
            if root.val == target:
                return None
            else:
                return root
        else:
            if root.val != target:
                root.left = self.removeLeafNodes(root.left,target)
                root.right = self.removeLeafNodes(root.right,target)
                return root
            else:
                l = self.removeLeafNodes(root.left,target)
                r = self.removeLeafNodes(root.right,target)
                if not l and not r:
                    return None
                else:
                    root.left = l
                    root.right = r
                    return root
