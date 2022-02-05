# Problem Id:  剑指 Offer 11
# Problem Name:  旋转数组的最小数字  LCOF, 旋转数组的最小数字
# Problem Url:  https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/
# Problem Level:  Easy
 
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if len(numbers) <= 2:
            return min(numbers)
        else:
            l = 0
            r = len(numbers) - 1
            mid = (l+r) // 2
            if numbers[mid] >= numbers[l] and numbers[r] >= numbers[mid] and numbers[l] != numbers[r]:
                return numbers[l]
            elif numbers[mid] == numbers[l] and numbers[mid] == numbers[r]:
                return min(self.minArray(numbers[:(mid+1)]),self.minArray(numbers[mid:]))
            elif numbers[mid] <= numbers[l] and numbers[mid] <= numbers[r]:
                return self.minArray(numbers[:(mid+1)])
            else:
                return self.minArray(numbers[mid:])