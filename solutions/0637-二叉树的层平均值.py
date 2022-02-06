# Problem Id:  637
# Problem Name:  Average of Levels in Binary Tree, 二叉树的层平均值
# Problem Url:  https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
# Problem Level:  Easy
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        def insert(root,i):
            if not root:
                pass
            else:
                if len(res) < i+1:
                    res.append([])
                res[i].append(root.val)
                insert(root.left,i+1)
                insert(root.right,i+1)
        insert(root,0)
        for i in range(len(res)):
            res[i] = sum(res[i])/len(res[i])
        return res
