# Problem Id:  剑指 Offer 33
# Problem Name:  二叉搜索树的后序遍历序列 LCOF, 二叉搜索树的后序遍历序列
# Problem Url:  https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
# Problem Level:  Medium
 
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 2:
            return True
        else:
            base = postorder[-1]
            index = -1
            for i in range(len(postorder)-1):
                if postorder[i] > base:
                    index = i
                    break
            if index == -1:
                return self.verifyPostorder(postorder[:(-1)])
            else:
                f = True
                for j in range(index,len(postorder)-1):
                    if postorder[j] < base:
                        f = False
                        break
                if f == False:
                    return False
                else:
                    return self.verifyPostorder(postorder[:index]) and self.verifyPostorder(postorder[index:(-1)])
                        
