# Problem Id:  1025
# Problem Name:  Divisor Game, 除数博弈
# Problem Url:  https://leetcode-cn.com/problems/divisor-game/
# Problem Level:  Easy
 
class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        elif N == 2:
            return True
        elif N == 3:
            return False
        else:
            save = [False, True , False]
            for i in range(3,N):
                temp = []
                for j in range(1,i+1):
                    if (i+1) % j == 0:
                        temp = temp + [i+1-j]
                result = False
                for j in range(len(temp)):
                    if save[temp[j]-1] == False:
                        result = True
                        break
                save = save + [result]

            return save[N-1]