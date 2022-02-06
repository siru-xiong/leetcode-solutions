# Problem Id:  1002
# Problem Name:  Find Common Characters, 查找共用字符
# Problem Url:  https://leetcode-cn.com/problems/find-common-characters/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        count = {}
        for i in range(len(A[0])):
            count[A[0][i]] = count.get(A[0][i],0) + 1
        for j in range(1,len(A)):
            temp_count = {}
            for i in range(len(A[j])):
                temp_count[A[j][i]] = temp_count.get(A[j][i],0) + 1
            ckey = list(count.keys())
            for i in range(len(ckey)):
                count[ckey[i]] = min(temp_count.get(ckey[i],0),count[ckey[i]])
        keys = list(count.keys())
        values = list(count.values())
        result = []
        for k in range(len(keys)):
            if values[k] != 0:
                result = result + [keys[k]] * values[k]
        return result