# Problem Id:  347
# Problem Name:  Top K Frequent Elements, 前 K 个高频元素
# Problem Url:  https://leetcode-cn.com/problems/top-k-frequent-elements/
# Problem Level:  Medium
 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = {}
        for i in nums:
            ct[i] = ct.get(i,0)+1
        ct = sorted(ct.items(), key = lambda x:x[1],reverse=True)
        return [i[0] for i in ct[:k]]
