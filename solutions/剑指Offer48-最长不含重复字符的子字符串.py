# Problem Id:  剑指 Offer 48
# Problem Name:  最长不含重复字符的子字符串 LCOF, 最长不含重复字符的子字符串
# Problem Url:  https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/
# Problem Level:  Medium
 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1
        start = 0
        end = 0
        curr_set = set(s[0])
        while end < len(s)-1:
            if s[end+1] not in curr_set:
                end += 1
                curr_set.add(s[end])
                res = max(res,len(curr_set))
            else:
                while s[start] != s[end+1]:
                    curr_set.remove(s[start])
                    start += 1
                start += 1
                end += 1
                curr_set.add(s[end])
                res = max(res,len(curr_set))
        return res
                