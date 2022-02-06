# Problem Id:  395
# Problem Name:  Longest Substring with At Least K Repeating Characters, 至少有 K 个重复字符的最长子串
# Problem Url:  https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/
# Problem Level:  Medium
# Language:  Python3
 
class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)