# Problem Id:  449
# Problem Name:  Serialize and Deserialize BST, 序列化和反序列化二叉搜索树
# Problem Url:  https://leetcode-cn.com/problems/serialize-and-deserialize-bst/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(rt):
            if not rt:
                pass
            else:
                dfs(rt.left)
                dfs(rt.right)
                res.append(rt.val)
        dfs(root)
        return res

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0 and len(postorder) == 0:
            return None
        if len(inorder) == 1 and len(postorder) == 1:
            return TreeNode(inorder[0])
        else:
            root = postorder[-1]
            for i in range(len(inorder)):
                if inorder[i] == root:
                    index = i
            leftinorder = inorder[:index]
            rightinorder = inorder[(index+1):]
            ln = len(leftinorder)
            leftpostorder = postorder[:ln]
            rightpostorder = postorder[ln:(-1)]
            return TreeNode(val= root,left= self.buildTree(leftinorder,leftpostorder),right = self.buildTree(rightinorder,rightpostorder))

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.
        """
        return '.'.join((str(i) for i in self.postorderTraversal(root)))
        

    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return None
        data = [int(i) for i in data.split('.')]
        postorder = data
        inorder = sorted(data)
        return self.buildTree(inorder, postorder)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans