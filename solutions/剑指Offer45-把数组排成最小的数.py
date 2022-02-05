# Problem Id:  剑指 Offer 45
# Problem Name:  把数组排成最小的数 LCOF, 把数组排成最小的数
# Problem Url:  https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/
# Problem Level:  Medium
 
class Solution:
    def comp(self,x,y):
        return int(str(x)+str(y)) <= int(str(y)+str(x))

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        elif len(nums) == 2:
            if self.comp(nums[0],nums[1]) == 0:
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
            if self.comp(n1[i],n2[j]):
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
    
    def minNumber(self, nums: List[int]) -> str:
        nums = self.sortArray(nums)
        res = ''
        for i in nums:
            res += str(i)
        return res