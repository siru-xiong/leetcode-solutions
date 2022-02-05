# Problem Id:  387
# Problem Name:  First Unique Character in a String, 字符串中的第一个唯一字符
# Problem Url:  https://leetcode-cn.com/problems/first-unique-character-in-a-string/
# Problem Level:  Easy
 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        result = -1
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                result = i
                break
        return result
            