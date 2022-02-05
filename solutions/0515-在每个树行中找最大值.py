# Problem Id:  515
# Problem Name:  Find Largest Value in Each Tree Row, 在每个树行中找最大值
# Problem Url:  https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root,i):
            if not root:
                pass
            else:
                while len(res) < i:
                    res.append(float('-inf'))
                res[i-1] = max(res[i-1],root.val)
                dfs(root.left,i+1)
                dfs(root.right,i+1)
        dfs(root,1)
        return res