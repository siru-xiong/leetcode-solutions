# Problem Id:  690
# Problem Name:  Employee Importance, 员工的重要性
# Problem Url:  https://leetcode-cn.com/problems/employee-importance/
# Problem Level:  Medium
 
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getsub(self,imp,sub,id):
        if sub[id] == []:
            return [id]
        else:
            result = [id]
            for i in range(len(sub[id])):
                result = result + self.getsub(imp,sub,sub[id][i])
            return result

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        sub = {}
        imp = {}
        for i in range(len(employees)):
            imp[employees[i].id] = employees[i].importance
            sub[employees[i].id] = employees[i].subordinates
        result = 0
        sub = self.getsub(imp,sub,id)
        for i in range(len(sub)):
            result = result + imp[sub[i]]
        return result