# Problem Id:  739
# Problem Name:  Daily Temperatures, 每日温度
# Problem Url:  https://leetcode-cn.com/problems/daily-temperatures/
# Problem Level:  Medium
 
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i in range(len(T)):
            if len(stack) == 0:
                stack.append((T[i],i))
            else:
                while len(stack) > 0 and stack[-1][0] < T[i]:
                    res[stack[-1][1]] = i - stack[-1][1]
                    del stack[-1]
                stack.append((T[i],i))
        return res