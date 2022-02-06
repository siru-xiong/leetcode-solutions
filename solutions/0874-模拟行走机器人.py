# Problem Id:  874
# Problem Name:  Walking Robot Simulation, 模拟行走机器人
# Problem Url:  https://leetcode-cn.com/problems/walking-robot-simulation/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direc = [[0,1],[-1,0],[0,-1],[1,0]]
        curr = [0,0]
        obstacles = set(map(tuple, obstacles))
        k = 0
        dist = 0
        for i in range(len(commands)):
            if commands[i] == -1:
                k = (k + 3) % 4
            elif commands[i]== -2:
                k = (k + 1) % 4
            else:
                for j in range(commands[i]):
                    curr[0] = curr[0] + direc[k][0]
                    curr[1] = curr[1] + direc[k][1]
                    if (curr[0],curr[1]) in obstacles:
                        curr[0] = curr[0] - direc[k][0]
                        curr[1] = curr[1] - direc[k][1]
                        break
                if curr[0]*curr[0] + curr[1]*curr[1] > dist:
                    dist = curr[0]*curr[0] + curr[1]*curr[1]
        return dist

                
