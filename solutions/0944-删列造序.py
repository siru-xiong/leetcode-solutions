# Problem Id:  944
# Problem Name:  Delete Columns to Make Sorted, 删列造序
# Problem Url:  https://leetcode-cn.com/problems/delete-columns-to-make-sorted/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if strs[j][i] < strs[j-1][i]:
                    count = count + 1
                    break
        return count