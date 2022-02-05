# Problem Id:  95
# Problem Name:  Unique Binary Search Trees II, 不同的二叉搜索树 II
# Problem Url:  https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def g2(self, r: List[int]) -> List[TreeNode]:
        if len(r) == 0:
            return [None]
        if len(r) == 1:
            return [TreeNode(r[0])]
        else:
            res = []
            for i in range(len(r)):
                left = self.g2(r[:i])
                right = self.g2(r[(i+1):])
                res = res + [TreeNode(val = r[i],left = x,right = y) for x in left for y in right]
            return res

    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.g2(range(1,n+1))