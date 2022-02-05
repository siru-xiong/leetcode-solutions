# Problem Id:  506
# Problem Name:  Relative Ranks, 相对名次
# Problem Url:  https://leetcode-cn.com/problems/relative-ranks/
# Problem Level:  Easy
 
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s = sorted(score, reverse = True)
        c = {}
        t = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i in range(len(s)):
            if i < 3:
                c[s[i]]  = t[i]
            else:
                c[s[i]] = str(i+1)
        for i in range(len(score)):
            score[i] = c[score[i]]
        return score