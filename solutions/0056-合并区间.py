# Problem Id:  56
# Problem Name:  Merge Intervals, 合并区间
# Problem Url:  https://leetcode-cn.com/problems/merge-intervals/
# Problem Level:  Medium
 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        def m(l1,l2):
            if l2[0] <=l1[1]:
                return [l1[0],max(l2[1],l1[1])]
            else:
                return False
        start = 0
        while start+1 < len(intervals):
            if m(intervals[start],intervals[start+1]) != False:
                intervals[start+1] = m(intervals[start],intervals[start+1])
                del intervals[start]
            else:
                start = start + 1
        return intervals
