# Problem Id:  60
# Problem Name:  Permutation Sequence, 排列序列
# Problem Url:  https://leetcode-cn.com/problems/permutation-sequence/
# Problem Level:  Hard
 
class Solution:

    def getp(self,nums,k):
        if len(nums) == 1:
            return nums
        elif len(nums) == 2:
            return [nums,[nums[1],nums[0]]][k-1]
        else:
            m = len(nums)
            t = [1,1,2,6,24,120,720,5040,40320,362880,3628800]
            a = (k-1) // t[m-1]
            r = (k-1) % t[m-1] + 1
            return [nums[a]] + self.getp(nums[:a]+nums[(a+1):],r)

    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1,n+1))
        return ''.join([str(i) for i in self.getp(nums,k)])
