# Problem Id:  17
# Problem Name:  Letter Combinations of a Phone Number, 电话号码的字母组合
# Problem Url:  https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        else:
            temp = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
            if len(digits) == 1:
                return list(temp[int(digits)-2])
            else:
                return [i+j for i in temp[int(digits[0])-2] for j in self.letterCombinations(digits[1:])]