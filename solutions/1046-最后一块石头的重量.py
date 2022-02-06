# Problem Id:  1046
# Problem Name:  Last Stone Weight, 最后一块石头的重量
# Problem Url:  https://leetcode-cn.com/problems/last-stone-weight/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones.sort(reverse=True)
            if stones[0] == stones[1]:
                del stones[0]
                del stones[0]
            else:
                stones[0] = stones[0] - stones[1]
                del stones[1]
        if len(stones) == 1:
            return stones[0]
        else:
            return 0