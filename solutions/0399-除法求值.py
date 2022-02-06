# Problem Id:  399
# Problem Name:  Evaluate Division, 除法求值
# Problem Url:  https://leetcode-cn.com/problems/evaluate-division/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ct = {}
        graph = {}
        for i in range(len(equations)):
            ct[(equations[i][0],equations[i][1])] = values[i]
            ct[(equations[i][1],equations[i][0])] = 1/values[i]
            if equations[i][0] not in graph:
                graph[equations[i][0]] = [equations[i][1]]
            else:
                graph[equations[i][0]].append(equations[i][1])
            if equations[i][1] not in graph:
                graph[equations[i][1]] = [equations[i][0]]
            else:
                graph[equations[i][1]].append(equations[i][0])
        def path(ct,start,end,past):
            if start == end:
                if start in graph:
                    return 1
                else:
                    return -1
            else:
                if start not in graph:
                    return -1
                else:
                    res = -1
                    temp = -1
                    for i in graph[start]:
                        if i not in past:
                            past.add(i)
                            temp = ct[(start,i)]*path(ct,i,end,past)
                            past.remove(i)
                            if temp > 0:
                                break
                    return temp
        output = []
        for i in queries:
            t = path(ct,i[0],i[1],set([i[0]]))
            if t < 0:
                output.append(-1)
            else:
                output.append(t)
        return output
                    




