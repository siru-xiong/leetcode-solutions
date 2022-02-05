# Problem Id:  781
# Problem Name:  Rabbits in Forest, 森林中的兔子
# Problem Url:  https://leetcode-cn.com/problems/rabbits-in-forest/
# Problem Level:  Medium
 
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        if len(answers) == 0:
            return 0
        ct = {}
        for i in answers:
            ct[i] = ct.get(i,0) + 1
        res = 0
        for i in ct:
            res = res + (i+1)*(ct[i] // (i+1))
            if ct[i] % (i+1) != 0:
                res += i + 1
        return res