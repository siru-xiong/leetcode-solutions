# Problem Id:  860
# Problem Name:  Lemonade Change, 柠檬水找零
# Problem Url:  https://leetcode-cn.com/problems/lemonade-change/
# Problem Level:  Easy
 
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ct = {}
        ct['5'] = 0
        ct['10'] = 0
        result = True
        for i in range(len(bills)):
            if bills[i] == 5:
                ct['5'] = ct['5'] + 1
            elif bills[i] == 10:
                ct['10'] = ct['10'] + 1
                ct['5'] = ct['5'] - 1
            elif bills[i] == 20:
                if ct['10'] >= 1 and ct['5'] >= 1:
                    ct['10'] = ct['10'] - 1
                    ct['5'] = ct['5'] - 1
                else:
                    ct['5'] = ct['5'] - 3
            if ct['5'] < 0 or ct['10'] <0:
                result = False
                break
        return result