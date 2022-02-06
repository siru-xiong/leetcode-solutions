# Problem Id:  1282
# Problem Name:  Group the People Given the Group Size They Belong To, 用户分组
# Problem Url:  https://leetcode-cn.com/problems/group-the-people-given-the-group-size-they-belong-to/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ct = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in ct:
                ct[groupSizes[i]].append(i)
            else:
                ct[groupSizes[i]] = [i]
        res = []
        for i in ct:
            t = 0
            while i*(t+1) <= len(ct[i]) :
                res.append(ct[i][t*i:i*(t+1)])
                t = t + 1
        return res
