# Problem Id:  面试题 04.03
# Problem Name:  List of Depth LCCI, 特定深度节点链表
# Problem Url:  https://leetcode-cn.com/problems/list-of-depth-lcci/
# Problem Level:  Medium
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def depth(self, tree):
        if not tree:
            return 0
        elif not tree.left and not tree.right:
            return 1
        else:
            return 1 + max(self.depth(tree.left),self.depth(tree.right))

    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        res = []
        d = self.depth(tree)
        head = [0] * d
        for j in range(d):
            res.append(ListNode(0))
            head[j] = res[j]
        def dfs(root,i):
            if not root:
                pass
            else:
                head[i].next = ListNode(root.val)
                head[i] = head[i].next
                dfs(root.left,i+1)
                dfs(root.right,i+1)
        dfs(tree,0)
        for i in range(len(res)):
            res[i] = res[i].next
        return res
    