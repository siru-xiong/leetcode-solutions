# Problem Id:  1630
# Problem Name:  Arithmetic Subarrays, 等差子数组
# Problem Url:  https://leetcode-cn.com/problems/arithmetic-subarrays/
# Problem Level:  Medium
 
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            check = nums[l[i]:(r[i]+1)]
            check.sort()
            t = True
            g = check[1] - check[0]
            for i in range(1,len(check)):
                if check[i] - check[i-1] != g:
                    t = False
                    break
            res.append(t)
        return res