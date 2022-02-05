# Problem Id:  剑指 Offer II 055
# Problem Name:  二叉搜索树迭代器, 二叉搜索树迭代器
# Problem Url:  https://leetcode-cn.com/problems/kTOapQ/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left


    def next(self) -> int:
        top = self.stack[-1]
        del self.stack[-1]
        if top.right:
            t = top.right
            while t:
                self.stack.append(t)
                t = t.left
        return top.val


    def hasNext(self) -> bool:
        return len(self.stack) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()