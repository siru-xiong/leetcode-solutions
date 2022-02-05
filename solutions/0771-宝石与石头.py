# Problem Id:  771
# Problem Name:  Jewels and Stones, 宝石与石头
# Problem Url:  https://leetcode-cn.com/problems/jewels-and-stones/
# Problem Level:  Easy
 
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = set(list(jewels))
        count = 0
        for i in range(len(stones)):
            if stones[i] in j:
                count = count + 1
        return count
