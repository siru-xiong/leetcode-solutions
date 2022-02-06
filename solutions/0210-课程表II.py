# Problem Id:  210
# Problem Name:  Course Schedule II, 课程表 II
# Problem Url:  https://leetcode-cn.com/problems/course-schedule-ii/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = {}
        for i in range(len(prerequisites)):
            if prerequisites[i][0] in pre:
                pre[prerequisites[i][0]].add(prerequisites[i][1])
            else:
                pre[prerequisites[i][0]] = set([prerequisites[i][1]])
        res = []
        rset = set()
        result = True
        while len(res) < numCourses:
            index = 0
            for i in range(numCourses):
                if (i not in pre and i not in rset) or (i in pre and i not in rset and len(pre[i])==0):
                    index = 1
                    res.append(i)
                    rset.add(i)
                    temp = i
                    break
            if index == 0 and len(rset) < numCourses:
                result = False
                break
            elif len(rset) < numCourses:
                if temp in pre:
                    del pre[temp]
                for k in pre:
                    if temp in pre[k]:
                        pre[k].remove(temp)
        if result == False:
            return []
        else:
            return res
