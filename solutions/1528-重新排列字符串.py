# Problem Id:  1528
# Problem Name:  Shuffle String, 重新排列字符串
# Problem Url:  https://leetcode-cn.com/problems/shuffle-string/
# Problem Level:  Easy
 
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        #ct = {}
        #for i in range(len(s)):
        #    ct[indices[i]] = s[i]
        #s = sorted(ct.items(),key=lambda x:x[0])
        #s = [x[1] for x in s]
        #s = ''.join(s)
        #return s
        result = [' ']*len(s)
        for i in range(len(s)):
            result[indices[i]] = s[i]
        return ''.join(result)
