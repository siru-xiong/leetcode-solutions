# Problem Id:  66
# Problem Name:  Plus One, 加一
# Problem Url:  https://leetcode-cn.com/problems/plus-one/
# Problem Level:  Easy
 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits == [0]:
            return [1]
        elif digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            for i in range(1,len(digits)+1):
                if digits[-i] == 9:
                    digits[-i] = 0
                else:
                    digits[-i] = digits[-i] + 1
                    break
            if digits[0] == 0:
                digits = [1] + digits
            return digits