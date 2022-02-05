# Problem Id:  1385
# Problem Name:  Find the Distance Value Between Two Arrays, 两个数组间的距离值
# Problem Url:  https://leetcode-cn.com/problems/find-the-distance-value-between-two-arrays/
# Problem Level:  Easy
 
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        for i in arr1:
            t = True
            for j in arr2:
                if j >= i - d and j <= i + d:
                    t = False
                    break
            if t == True:
                res += 1
        return res
