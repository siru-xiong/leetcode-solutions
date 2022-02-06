# Problem Id:  LCP 01
# Problem Name:  Guess Numbers, 猜数字
# Problem Url:  https://leetcode-cn.com/problems/guess-numbers/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return (guess[0]==answer[0])+(guess[1]==answer[1])+(guess[2]==answer[2])