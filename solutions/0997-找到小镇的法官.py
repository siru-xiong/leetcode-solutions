# Problem Id:  997
# Problem Name:  Find the Town Judge, 找到小镇的法官
# Problem Url:  https://leetcode-cn.com/problems/find-the-town-judge/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        result = [0] * N
        for i in range(len(trust)):
            result[trust[i][1]-1] = result[trust[i][1]-1] + 1
            result[trust[i][0]-1] = result[trust[i][0]-1] - 1
        judge = -1
        for i in range(N):
            if result[i] == N-1:
                judge = i + 1
                break
        return judge
        #ss = set([x[0] for x in trust])
        #if len(ss) != N-1:
        #    return -1
        #else:
            #for i in range(1,N+1):
            #    if i not in ss:
            #        p = i
            #plist = []
            #for i in range(len(trust)):
            #    if trust[i][1] == p:
            #        plist.append(trust[i][0])
            #if len(set(plist)) == N - 1 and p not in set(plist):
            #    return p
            #else:
            #    return -1
