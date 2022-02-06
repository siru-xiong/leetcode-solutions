# Problem Id:  881
# Problem Name:  Boats to Save People, 救生艇
# Problem Url:  https://leetcode-cn.com/problems/boats-to-save-people/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        i = 0
        j = len(people)-1
        while i <= j:
            if i == j:
                res += 1
                break
            elif people[i] + people[j] <= limit:
                res += 1
                i += 1
                j -= 1
            else:
                res += 1
                j -= 1
        return res