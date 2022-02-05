# Problem Id:  821
# Problem Name:  Shortest Distance to a Character, 字符的最短距离
# Problem Url:  https://leetcode-cn.com/problems/shortest-distance-to-a-character/
# Problem Level:  Easy
 
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [0] * len(s)
        t = []
        for i in range(len(s)):
            if s[i] == c:
                t.append(i)
        if len(t) == 1:
            return [abs(i-t[0]) for i in range(len(s))]
        start = 1
        for i in range(len(s)):
            if i <= t[start]:
                res[i] = min(abs(i-t[start]),abs(i-t[start-1]))
            else:
                if start < len(t) - 1:
                    start += 1
                res[i] = min(abs(i-t[start]),abs(i-t[start-1]))
        return res