# Problem Id:  763
# Problem Name:  Partition Labels, 划分字母区间
# Problem Url:  https://leetcode-cn.com/problems/partition-labels/
# Problem Level:  Medium
 
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ct = {}
        for i in range(len(S)):
            ct[S[i]] = i
        res = []
        start = 0
        while start < len(S):
            end = ct[S[start]]
            i = start
            while i <= end:
                if ct[S[i]] >= end:
                    end = ct[S[i]]
                    i = i + 1
                else:
                    i = i + 1
            res.append(end-start+1)
            start = end + 1
        return res
        


            