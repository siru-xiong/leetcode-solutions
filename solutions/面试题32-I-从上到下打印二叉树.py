# Problem Id:  面试题32 - I
# Problem Name:  从上到下打印二叉树 LCOF, 从上到下打印二叉树
# Problem Url:  https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root,i):
            if not root:
                return
            while len(res) < i:
                res.append([])
            res[i-1].append(root.val)
            dfs(root.left,i+1)
            dfs(root.right,i+1)
        dfs(root,1)
        resu = []
        for i in res:
            resu += i
        return resu