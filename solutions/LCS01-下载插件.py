# Problem Id:  LCS 01
# Problem Name:  下载插件, 下载插件
# Problem Url:  https://leetcode-cn.com/problems/Ju9Xwi/
# Problem Level:  Easy
 
class Solution:
    def leastMinutes(self, n: int) -> int:
        res = 0
        speed = 1
        while speed < n:
            res += 1
            speed *= 2
        return res + 1