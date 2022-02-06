# Problem Id:  889
# Problem Name:  Construct Binary Tree from Preorder and Postorder Traversal, 根据前序和后序遍历构造二叉树
# Problem Url:  https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0 and len(post) == 0:
            return None
        elif len(pre) == 1 and len(post) == 1:
            return TreeNode(val=pre[0])
        else:
            for i in range(len(post)):
                if post[i] == pre[1]:
                    break
            left = self.constructFromPrePost(pre[1:(i+2)],post[:(i+1)])
            right = self.constructFromPrePost(pre[(i+2):],post[(i+1):(-1)])
            return TreeNode(val=pre[0],left=left,right=right)
            