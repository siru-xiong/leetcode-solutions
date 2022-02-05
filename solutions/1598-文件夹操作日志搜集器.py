# Problem Id:  1598
# Problem Name:  Crawler Log Folder, 文件夹操作日志搜集器
# Problem Url:  https://leetcode-cn.com/problems/crawler-log-folder/
# Problem Level:  Easy
 
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in logs:
            if i == '../':
                count = max(count - 1,0)
            elif i == './':
                pass
            else:
                count = count + 1
        return count