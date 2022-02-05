# Problem Id:  1469
# Problem Name:  Find All The Lonely Nodes, 寻找所有的独生节点
# Problem Url:  https://leetcode-cn.com/problems/find-all-the-lonely-nodes/
# Problem Level:  Easy
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        if not root or (not root.left and not root.right):
            return []
        else:
            if not root.left and root.right:
                res = [root.right.val]
            elif not root.right and root.left:
                res = [root.left.val]
            else:
                res = []
            res = res + self.getLonelyNodes(root.left) +  self.getLonelyNodes(root.right)
            return res
