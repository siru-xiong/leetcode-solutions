# Problem Id:  1688
# Problem Name:  Count of Matches in Tournament, 比赛中的配对次数
# Problem Url:  https://leetcode-cn.com/problems/count-of-matches-in-tournament/
# Problem Level:  Easy
 
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1
        #if n == 1:
        #    return 0
        #elif n == 2:
        #    return 1
        #else:
        #    if n % 2 == 0:
        #        return int(n/2)+self.numberOfMatches(int(n/2))
        #    else:
        #        return int((n-1)/2)+self.numberOfMatches(int((n-1)/2)+1)