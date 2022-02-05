# Problem Id:  159
# Problem Name:  Longest Substring with At Most Two Distinct Characters, 至多包含两个不同字符的最长子串
# Problem Url:  https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters/
# Problem Level:  Medium
 
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        dic = set()
        res=0
        l=0
        for i in range(len(s)):
            if s[i] in dic:
                pass
            elif len(dic) < 2:
                dic.add(s[i])
            else:
                l = i - 1
                while l-1 >= 0 and s[l-1] == s[l]:
                    l = l - 1
                dic = set(s[(i-1):(i+1)])
            res=max(res,i-l+1)
        return res