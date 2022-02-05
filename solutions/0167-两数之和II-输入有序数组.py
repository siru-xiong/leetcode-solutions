# Problem Id:  167
# Problem Name:  Two Sum II - Input Array Is Sorted, 两数之和 II - 输入有序数组
# Problem Url:  https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
# Problem Level:  Medium
 
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
        return [i+1,j+1]

           
