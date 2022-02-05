# Problem Id:  1047
# Problem Name:  Remove All Adjacent Duplicates In String, 删除字符串中的所有相邻重复项
# Problem Url:  https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/
# Problem Level:  Easy
 
class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        for i in list(S):
            if len(res) == 0:
                res.append(i)
            else:
                if i == res[-1]:
                    del res[-1]
                else:
                    res.append(i)
        return ''.join(res)