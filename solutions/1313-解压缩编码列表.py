# Problem Id:  1313
# Problem Name:  Decompress Run-Length Encoded List, 解压缩编码列表
# Problem Url:  https://leetcode-cn.com/problems/decompress-run-length-encoded-list/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums) // 2
        res = []
        for i in range(n):
            res.extend([nums[2*i+1]]*nums[2*i])
        return res