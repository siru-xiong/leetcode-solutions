# Problem Id:  297
# Problem Name:  Serialize and Deserialize Binary Tree, 二叉树的序列化与反序列化
# Problem Url:  https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
# Problem Level:  Hard
 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val,[],[]]
        else:
            l = self.serialize(root.left)
            r = self.serialize(root.right)
            return [root.val,l,r]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == []:
            return None
        elif len(data) == 3 and data[1] == [] and data[2] == []:
            return TreeNode(val=data[0])
        else:
            res = TreeNode(data[0])
            res.left = self.deserialize(data[1])
            res.right = self.deserialize(data[2])
            return res
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))