# Problem Id:  1395
# Problem Name:  Count Number of Teams, 统计作战单位数
# Problem Url:  https://leetcode-cn.com/problems/count-number-of-teams/
# Problem Level:  Medium
 
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(1,len(rating)-1):
            a = 0
            b = 0
            c = 0
            d = 0
            for k in range(i):
                if rating[k] < rating[i]:
                    a += 1
                if rating[k] > rating[i]:
                    b += 1
            for k in range(i+1,len(rating)):
                if rating[k] < rating[i]:
                    c += 1
                if rating[k] > rating[i]:
                    d += 1
            res += a*d+b*c
        return res