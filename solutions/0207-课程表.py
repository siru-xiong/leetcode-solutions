# Problem Id:  207
# Problem Name:  Course Schedule, 课程表
# Problem Url:  https://leetcode-cn.com/problems/course-schedule/
# Problem Level:  Medium
 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        a = set()
        pre = {}
        explored = set()
        for i in range(len(prerequisites)):
            pre[prerequisites[i][0]] = pre.get(prerequisites[i][0],[]) + [prerequisites[i][1]]
        def dfs(past,start,d):
            if start in explored:
                return True
            else:
                explored.add(start)
                if start not in d:
                    return True
                else:
                    result = True
                    for i in d[start]:
                        if i not in past and i != start:
                            past.add(start)
                            result = result and dfs(past,i,d)
                            past.remove(start)
                        else:
                            result = False
                            break
                    return result
        res = True
        for i in pre:
            res = res and dfs(set(),i,pre)
        return res
