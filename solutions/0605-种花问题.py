# Problem Id:  605
# Problem Name:  Can Place Flowers, 种花问题
# Problem Url:  https://leetcode-cn.com/problems/can-place-flowers/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        flowerbed = [0] + flowerbed + [0]
        count = 0
        for i in range(1,length+1):
            if sum(flowerbed[(i-1):(i+2)]) == 0:
                flowerbed[i] = 1
                count = count + 1
        return n <= count