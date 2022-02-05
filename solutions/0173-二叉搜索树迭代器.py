# Problem Id:  173
# Problem Name:  Binary Search Tree Iterator, 二叉搜索树迭代器
# Problem Url:  https://leetcode-cn.com/problems/binary-search-tree-iterator/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftmost_inorder(root)

    def next(self) -> int:
        topmost_node = self.stack.pop()
        if topmost_node.right:
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()