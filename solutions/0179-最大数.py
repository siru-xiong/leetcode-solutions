# Problem Id:  179
# Problem Name:  Largest Number, 最大数
# Problem Url:  https://leetcode-cn.com/problems/largest-number/
# Problem Level:  Medium
 
class Solution:
    def compare(self,x,y):
        return int(x+y) > int(y+x)

    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        nums = self.sortArray(nums)
        nums = ''.join(nums)
        nums = list(nums)
        while nums[0] == '0':
            if len(nums) > 1:
                del nums[0]
            else:
                break
        return ''.join(nums)

    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        elif len(nums) == 2:
            if self.compare(nums[0],nums[1]) == 0:
                nums[0],nums[1] = nums[1],nums[0]
            return nums
        else:
            ind = len(nums)//2
            left = self.sortArray(nums[:ind])
            right = self.sortArray(nums[ind:])
            return self.merge(left,right)

    def merge(self,n1,n2):
        res = []
        i = 0
        j = 0
        while i < len(n1) and j < len(n2):
            if self.compare(n1[i],n2[j]) == 1:
                res.append(n1[i])
                i += 1
            else:
                res.append(n2[j])
                j += 1
        if i < len(n1):
            res = res + n1[i:]
        if j < len(n2):
            res = res + n2[j:]
        return res