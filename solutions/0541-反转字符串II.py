# Problem Id:  541
# Problem Name:  Reverse String II, 反转字符串 II
# Problem Url:  https://leetcode-cn.com/problems/reverse-string-ii/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        leng = len(s)
        times = leng // (2*k)
        left = leng % (2*k)
        s = list(s)
        for i in range(times):
            s[2*k*i:(2*k*i+k)] = s[2*k*i:(2*k*i+k)][::-1]
        if left == 0:
            pass
        elif left <= k:
            s[2*k*times:] = s[2*k*times:][::-1]
        else:
            s[2*k*times:(2*k*times+k)] = s[2*k*times:(2*k*times+k)][::-1]
        return ''.join(s)