# Problem Id:  501
# Problem Name:  Find Mode in Binary Search Tree, 二叉搜索树中的众数
# Problem Url:  https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ct = {}
        def count(root):
            if not root:
                pass
            else:
                ct[root.val] = ct.get(root.val,0) + 1
                count(root.left)
                count(root.right)
        count(root)
        vmax = 0
        result = []
        ct = list(ct.items())
        for i in ct:
            if i[1] > vmax:
                result = []
                result.append(i[0])
                vmax = i[1]
            elif i[1] == vmax:
                result.append(i[0])
        return result