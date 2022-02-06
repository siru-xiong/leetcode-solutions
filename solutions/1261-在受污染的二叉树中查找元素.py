# Problem Id:  1261
# Problem Name:  Find Elements in a Contaminated Binary Tree, 在受污染的二叉树中查找元素
# Problem Url:  https://leetcode-cn.com/problems/find-elements-in-a-contaminated-binary-tree/
# Problem Level:  Medium
# Language:  Python3
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:
    def addt(self, root: TreeNode, v: int) -> TreeNode:
        if not root:
            return None
        else:
            root.val += v
            root.left = self.addt(root.left,2*v)
            root.right = self.addt(root.right,2*v)
            return root
    
    def rec(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            l = self.rec(root.left)
            r = self.rec(root.right)
            root.val = 0
            if root.left:
                root.left = self.addt(l,1)
            if root.right:
                root.right = self.addt(r,2)
            return root

    def el(self, root: TreeNode) -> TreeNode:
        if not root:
            pass
        else:
            self.elements.append(root.val)
            self.el(root.left)
            self.el(root.right)    

    def __init__(self, root: TreeNode):
        self.elements = []
        self.recover = self.rec(root)
        self.el(self.recover)

    def find(self, target: int) -> bool:
        return target in self.elements
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)