# Problem Id:  1394
# Problem Name:  Find Lucky Integer in an Array, 找出数组中的幸运数
# Problem Url:  https://leetcode-cn.com/problems/find-lucky-integer-in-an-array/
# Problem Level:  Easy
 
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ct = {}
        for i in arr:
            ct[i] = ct.get(i,0) + 1
        res = -1
        for i in arr:
            if ct[i] == i and i > res:
                res = i
        return res