# Problem Id:  面试题 01.05
# Problem Name:  One Away LCCI, 一次编辑
# Problem Url:  https://leetcode-cn.com/problems/one-away-lcci/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        ct = {}
        if len(first) == 0:
            return len(second) <= 1
        if len(second) == 0:
            return len(first) <= 1

        if first[0] == second[0]:
            ct[(0,0)] = 0
        else:
            ct[(0,0)] = 1

        for i in range(1,len(first)):
            if first[i] == second[0]:
                ct[(i,0)] = ct[(i-1,0)]
            else:
                ct[(i,0)] = ct[(i-1,0)] + 1
        
        for j in range(1,len(second)):
            if second[j] == first[0]:
                ct[(0,j)] = ct[(0,j-1)]
            else:
                ct[(0,j)] = ct[(0,j-1)] + 1
                
        for i in range(1,len(first)):
            for j in range(1,len(second)):
                if first[i] == second[j]:
                    ct[(i,j)] = ct[(i-1,j-1)]
                else:
                    t1 = ct[(i-1,j)] + 1
                    t2 = ct[(i,j-1)] + 1
                    t3 = ct[(i-1,j-1)] + 1
                    ct[(i,j)] = min(t1,t2,t3)
        
        return ct[(len(first)-1,len(second)-1)] <= 1
