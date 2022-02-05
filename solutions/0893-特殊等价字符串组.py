# Problem Id:  893
# Problem Name:  Groups of Special-Equivalent Strings, 特殊等价字符串组
# Problem Url:  https://leetcode-cn.com/problems/groups-of-special-equivalent-strings/
# Problem Level:  Medium
 
class Solution:
    def t(self, x):
        a = x[0::2]
        b = x[1::2]
        u = [0] * 26
        v = [0] * 26
        for i in a:
            u[ord(i)-97] += 1
        for i in b:
            v[ord(i)-97] += 1
        return tuple(u + v)

    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res = set()
        for i in A:
            res.add(self.t(i))
        return len(res)