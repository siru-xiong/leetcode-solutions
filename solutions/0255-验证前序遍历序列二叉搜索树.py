# Problem Id:  255
# Problem Name:  Verify Preorder Sequence in Binary Search Tree, 验证前序遍历序列二叉搜索树
# Problem Url:  https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree/
# Problem Level:  Medium
 
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        rec = []
        t = float()
        for i in preorder:
            if len(rec) != 0:
                while len(rec) > 0 and rec[-1] < i:
                    t = rec[-1]
                    del rec[-1]
            if i < t:
                return False
            rec.append(i)
        return True