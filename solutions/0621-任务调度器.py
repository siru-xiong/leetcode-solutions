# Problem Id:  621
# Problem Name:  Task Scheduler, 任务调度器
# Problem Url:  https://leetcode-cn.com/problems/task-scheduler/
# Problem Level:  Medium
 
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        else:
            ct = {}
            for i in range(len(tasks)):
                ct[tasks[i]] = ct.get(tasks[i],0) + 1
            res = []
            r = 0
            while True:
                inv = set(res[(-n):])
                temp = float('-inf')
                b = True
                for i in ct:
                    if ct[i] > 0:
                        b = False
                    if i not in inv:
                        if ct[i] > 0 and ct[i] > temp:
                            temp = ct[i]
                            select = i
                if b == True:
                    break
                if temp == float('-inf'):
                    res.append('-')
                    r = r + 1
                else:
                    ct[select] -= 1
                    res.append(select)
                    r = r + 1
                res = res[(-n):]
            return r


            
            