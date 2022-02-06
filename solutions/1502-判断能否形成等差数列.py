# Problem Id:  1502
# Problem Name:  Can Make Arithmetic Progression From Sequence, 判断能否形成等差数列
# Problem Url:  https://leetcode-cn.com/problems/can-make-arithmetic-progression-from-sequence/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        gap = arr[1] - arr[0]
        result = True
        for i in range(2,len(arr)):
            if arr[i] - arr[i-1] != gap:
                result = False
                break
        return result