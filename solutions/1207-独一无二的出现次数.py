# Problem Id:  1207
# Problem Name:  Unique Number of Occurrences, 独一无二的出现次数
# Problem Url:  https://leetcode-cn.com/problems/unique-number-of-occurrences/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in range(len(arr)):
            count[arr[i]] = count.get(arr[i],0) + 1
        return len(set(count.values())) == len(count.values())
