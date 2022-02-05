# Problem Id:  543
# Problem Name:  Diameter of Binary Tree, 二叉树的直径
# Problem Url:  https://leetcode-cn.com/problems/diameter-of-binary-tree/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.ans - 1
    
    def depth(self, node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = self.depth(node.left)
            # 右儿子为根的子树的深度
            R = self.depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1