# Problem Id:  70
# Problem Name:  Climbing Stairs, 爬楼梯
# Problem Url:  https://leetcode-cn.com/problems/climbing-stairs/
# Problem Level:  Easy
 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            save = [1,2]
            for i in range(2,n):
                save = save + [save[i-1] + save[i-2]]
            return save[n-1]