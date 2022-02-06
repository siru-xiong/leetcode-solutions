# Problem Id:  1276
# Problem Name:  Number of Burgers with No Waste of Ingredients, 不浪费原料的汉堡制作方案
# Problem Url:  https://leetcode-cn.com/problems/number-of-burgers-with-no-waste-of-ingredients/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        t = tomatoSlices
        c = cheeseSlices
        if (t-2*c) % 2 == 0 and (t- 2*c) // 2 >=0 and (4*c-t) % 2 == 0 and (4*c-t) // 2 >= 0:
            return [(t- 2*c) // 2, (4*c-t) // 2]
        else:
            return []