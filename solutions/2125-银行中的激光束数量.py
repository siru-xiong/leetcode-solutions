# Problem Id:  2125
# Problem Name:  Number of Laser Beams in a Bank, 银行中的激光束数量
# Problem Url:  https://leetcode-cn.com/problems/number-of-laser-beams-in-a-bank/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [sum([int(x) for x in b]) for b in bank]
        if sum([i>0 for i in bank]) <= 1:
            return 0
        else:
            res = 0
            while bank[0] == 0:
                del bank[0]
            first = bank[0]
            for i in range(1,len(bank)):
                if bank[i] != 0:
                    res += bank[i]*first
                    first = bank[i]
            return res