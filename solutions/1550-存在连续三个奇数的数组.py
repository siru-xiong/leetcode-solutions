# Problem Id:  1550
# Problem Name:  Three Consecutive Odds, 存在连续三个奇数的数组
# Problem Url:  https://leetcode-cn.com/problems/three-consecutive-odds/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 0
        while i <= len(arr)-3:
            if arr[i] & 1:
                if arr[i+1] & 1:
                    if arr[i+2] & 1:
                        return True
                    else:
                        i += 3
                else:
                    i += 2
            else:
                i += 1
        return False
