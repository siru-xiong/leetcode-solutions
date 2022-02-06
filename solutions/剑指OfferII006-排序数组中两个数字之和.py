# Problem Id:  剑指 Offer II 006
# Problem Name:  排序数组中两个数字之和, 排序数组中两个数字之和
# Problem Url:  https://leetcode-cn.com/problems/kLl5u1/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while True:
            if numbers[i] + numbers[j] > target:
                j = j - 1
            elif numbers[i] + numbers[j] < target:
                i = i + 1
            else:
                break
        return [i,j]