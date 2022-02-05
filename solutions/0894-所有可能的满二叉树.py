# Problem Id:  894
# Problem Name:  All Possible Full Binary Trees, 所有可能的满二叉树
# Problem Url:  https://leetcode-cn.com/problems/all-possible-full-binary-trees/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        res = []
        for i in range(N+1):
            res.append([])
        res[1] = [TreeNode(0)]
        for j in range(2,N+1):
            for k in range(1,j-1):
                a = res[k]
                b = res[j-k-1]
                for x in a:
                    for y in b:
                        t = TreeNode(0)
                        t.left = x
                        t.right = y
                        res[j].append(t)
        return res[-1]