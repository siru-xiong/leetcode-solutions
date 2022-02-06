# Problem Id:  剑指 Offer II 035
# Problem Name:  最小时间差, 最小时间差
# Problem Url:  https://leetcode-cn.com/problems/569nqc/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort(key=lambda x:int(x[:x.find(':')])*60+int(x[(x.find(':')+1):]))
        res = float("inf")
        for i in range(len(timePoints)-1):
            f = timePoints[i]
            s = timePoints[i+1]
            res = min(res,(int(s[:s.find(':')])-int(f[:f.find(':')]))*60+int(s[(s.find(':')+1):])-int(f[(f.find(':')+1):]))
        f = timePoints[0]
        s = timePoints[-1]
        res = min(res,1440-((int(s[:s.find(':')])-int(f[:f.find(':')]))*60+int(s[(s.find(':')+1):])-int(f[(f.find(':')+1):])))
        return res
