# Problem Id:  107
# Problem Name:  Binary Tree Level Order Traversal II, 二叉树的层序遍历 II
# Problem Url:  https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        def dfx(root,i):
            if not root:
                pass
            elif not root.left and not root.right:
                if len(result) < i + 1:
                    for j in range(i+1-len(result)):
                        result.append([])
                result[i].append(root.val)
            else:
                if len(result) < i + 1:
                    for j in range(i+1-len(result)):
                        result.append([])
                result[i].append(root.val)
                if root.left:
                    dfx(root.left,i+1)
                if root.right: 
                    dfx(root.right,i+1)
        dfx(root,0)
        return result[::-1]
