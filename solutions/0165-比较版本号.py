# Problem Id:  165
# Problem Name:  Compare Version Numbers, 比较版本号
# Problem Url:  https://leetcode-cn.com/problems/compare-version-numbers/
# Problem Level:  Medium
 
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = -1
        j = -1
        for k in range(len(version1)):
            if version1[k] == '.':
                i = k
                break
        for k in range(len(version2)):
            if version2[k] == '.':
                j = k
                break
        if i == -1 and j == -1:
            if float(version1) < float(version2):
                return -1
            elif float(version1) > float(version2):
                return 1
            else:
                return 0
        elif i == -1:
            x = float(version1)
            y = float(version2[:j])
            if x == y:
                return self.compareVersion('0',version2[(j+1):])
            elif x > y:
                return 1
            else:
                return -1
        elif j == -1:
            x = float(version1[:i])
            y = float(version2)
            if x == y:
                return self.compareVersion(version1[(i+1):],'0')
            elif x > y:
                return 1
            else:
                return -1
        else:
            x = float(version1[:i])
            y = float(version2[:j])
            if x == y:
                return self.compareVersion(version1[(i+1):],version2[(j+1):])
            elif x > y:
                return 1
            else:
                return -1