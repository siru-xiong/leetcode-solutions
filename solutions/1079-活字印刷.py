# Problem Id:  1079
# Problem Name:  Letter Tile Possibilities, 活字印刷
# Problem Url:  https://leetcode-cn.com/problems/letter-tile-possibilities/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def cp(self,ct) -> int:
        r = 0
        for i in ct:
            r = max(r,ct[i])
        if r == 0:
            return 0
        else:
            res = 0
            for i in ct:
                if ct[i] > 0:
                    res += 1
                    ct[i] -= 1
                    res += self.cp(ct)
                    ct[i] += 1
            return res

    def numTilePossibilities(self, tiles: str) -> int:
        ct = {}
        for i in tiles:
            ct[i] = ct.get(i,0) + 1
        return self.cp(ct)