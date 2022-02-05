# Problem Id:  剑指 Offer 32 - II
# Problem Name:  从上到下打印二叉树 II LCOF, 从上到下打印二叉树 II
# Problem Url:  https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(tree,start = 1):
            if not tree:
                pass
            else:
                while len(res) < start:
                    res.append([])
                res[start-1].append(tree.val)
                dfs(tree.left,start+1)
                dfs(tree.right,start+1)
        dfs(root)
        return res