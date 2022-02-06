# Problem Id:  剑指 Offer 31
# Problem Name:  栈的压入、弹出序列 LCOF, 栈的压入、弹出序列
# Problem Url:  https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = set(popped)
        r = 0
        res = []
        for i in pushed:
            res.append(i)
            if i == popped[r]:
                del res[-1]
                r = r + 1
                while len(res) > 0 and res[-1] in s:
                    if res[-1] == popped[r]:
                        del res[-1]
                        r = r + 1
                    else:
                        break
        return res == []
