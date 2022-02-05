# Problem Id:  3
# Problem Name:  Longest Substring Without Repeating Characters, 无重复字符的最长子串
# Problem Url:  https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# Problem Level:  Medium
 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        end = 0
        window = set(s[start])
        res = 1
        while end+1 < len(s):
            if s[end+1] not in window:
                window.add(s[end+1])
                end = end + 1
                res = max(res,end-start+1)
            else:
                while s[start] != s[end+1]:
                    window.remove(s[start])
                    start = start + 1
                start = start + 1
                end = end + 1
        return res

