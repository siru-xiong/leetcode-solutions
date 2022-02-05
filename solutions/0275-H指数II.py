# Problem Id:  275
# Problem Name:  H-Index II, H 指数 II
# Problem Url:  https://leetcode-cn.com/problems/h-index-ii/
# Problem Level:  Medium
 
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0 
        r = len(citations)-1
        length = len(citations)
        while r > l+1:
            mid = (l+r) // 2
            if citations[mid] <= length-mid:
                l = mid
            else:
                r = mid
        if citations[r] <= length-r:
            return citations[r]
        elif citations[l] <= length-l:
            return max(citations[l],length-r)
        else:
            return length
