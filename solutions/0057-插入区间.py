# Problem Id:  57
# Problem Name:  Insert Interval, 插入区间
# Problem Url:  https://leetcode-cn.com/problems/insert-interval/
# Problem Level:  Medium
 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        t = -1
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[0]:
                t = i
            else:
                break
        r = -1
        for i in range(len(intervals)):
            if intervals[i][0] <= newInterval[1]:
                r = i
            else:
                break
        if t == -1 and r == -1:
            return [newInterval] + intervals
        elif t == -1:
            return [[newInterval[0],max(intervals[r][1],newInterval[1])]] + intervals[(r+1):]
        else:
            if intervals[t][1] < newInterval[0]:
                return intervals[:(t+1)] + [[newInterval[0],max(newInterval[1],intervals[r][1])]] + intervals[(r+1):]
            else:
                return intervals[:t] + [[intervals[t][0],max(newInterval[1],intervals[r][1])]] + intervals[(r+1):]