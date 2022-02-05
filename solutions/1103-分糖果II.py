# Problem Id:  1103
# Problem Name:  Distribute Candies to People, 分糖果 II
# Problem Url:  https://leetcode-cn.com/problems/distribute-candies-to-people/
# Problem Level:  Easy
 
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0]  * num_people
        i = 1
        index = 0
        while True:
            if candies >= i:
                res[index] = res[index]+i
                candies = candies - i
                i = i + 1
                index = (index + 1) % num_people
            else:
                break
        res[index] = res[index] + candies
        return res