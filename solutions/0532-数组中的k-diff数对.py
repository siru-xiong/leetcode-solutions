# Problem Id:  532
# Problem Name:  K-diff Pairs in an Array, 数组中的 k-diff 数对
# Problem Url:  https://leetcode-cn.com/problems/k-diff-pairs-in-an-array/
# Problem Level:  Medium
 
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            r = {}
            for i in nums:
                r[i] = r.get(i,0)+1
            res = 0
            for i in r:
                if r[i] > 1:
                    res += 1
            return res
        else:
            res = 0
            n = set(nums)
            for i in n:
                if i+k in n:
                    res += 1
            return res