# Problem Id:  337
# Problem Name:  House Robber III, 打家劫舍 III
# Problem Url:  https://leetcode-cn.com/problems/house-robber-iii/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dict = {}
        self.dict[None] = 0

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            self.dict[root] = root.val
            return root.val
        else:
            s1 = root.val
            if root.left:
                if root.left.left in self.dict:
                    s1 += self.dict[root.left.left]
                else:
                    t = self.rob(root.left.left)
                    self.dict[root.left.left] = t
                    s1 += t
                if root.left.right in self.dict:
                    s1 += self.dict[root.left.right]
                else:
                    t = self.rob(root.left.right)
                    self.dict[root.left.right] = t
                    s1 += t
            if root.right:
                if root.right.left in self.dict:
                    s1 += self.dict[root.right.left]
                else:
                    t = self.rob(root.right.left)
                    self.dict[root.right.left] = t
                    s1 += t
                if root.right.right in self.dict:
                    s1 += self.dict[root.right.right]
                else:
                    t = self.rob(root.right.right)
                    self.dict[root.right.right] = t
                    s1 += t
            s2 = 0
            if root.left in self.dict:
                s2 += self.dict[root.left]
            else:
                t = self.rob(root.left)
                self.dict[root.left] = t
                s2 += t
            if root.right in self.dict:
                s2 += self.dict[root.right]
            else:
                t = self.rob(root.right)
                self.dict[root.right] = t
                s2 += t
            return max(s1,s2)