# Problem Id:  830
# Problem Name:  Positions of Large Groups, 较大分组的位置
# Problem Url:  https://leetcode-cn.com/problems/positions-of-large-groups/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        if len(s) <= 2:
            return []
        elif len(s) == 3:
            if s[0] == s[1] and s[1] == s[2]:
                return [[0,2]]
            else:
                return []
        else:
            curr = s[0]
            start = 0
            result = []
            for i in range(1,len(s)):
                if s[i] != curr:
                    if i-1-start >= 2:
                        result = result + [[start,i-1]]
                    start = i
                    curr = s[i]
            if len(s)-2-start >= 1:
                result = result + [[start,len(s)-1]]
            return result

