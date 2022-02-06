# Problem Id:  1790
# Problem Name:  Check if One String Swap Can Make Strings Equal, 仅执行一次字符串交换能否使两个字符串相等
# Problem Url:  https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        t1 = []
        t2 = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                t1.append(s1[i])
                t2.append(s2[i])
        if len(t1) == 0:
            return True
        elif len(t1) == 2:
            return t1[0] == t2[1] and t1[1] == t2[0]
        else:
            return False
