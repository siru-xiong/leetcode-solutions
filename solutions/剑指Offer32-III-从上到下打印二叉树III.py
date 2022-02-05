# Problem Id:  剑指 Offer 32 - III
# Problem Name:  从上到下打印二叉树 III LCOF, 从上到下打印二叉树 III
# Problem Url:  https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(root,i,j):
            if not root:
                return
            while len(res) < i:
                res.append([])
            left = dfs(root.left,i+1,1-j)
            right = dfs(root.right,i+1,1-j)
            if j == 0:
                res[i-1] = res[i-1] + [root.val]
            else:
                res[i-1] = [root.val] + res[i-1]
        dfs(root,1,0)
        return res