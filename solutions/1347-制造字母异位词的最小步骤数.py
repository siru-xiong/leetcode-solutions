# Problem Id:  1347
# Problem Name:  Minimum Number of Steps to Make Two Strings Anagram, 制造字母异位词的最小步骤数
# Problem Url:  https://leetcode-cn.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
# Problem Level:  Medium
 
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = [0] * 26
        c2 = [0] * 26
        for i in s:
            c1[ord(i)-ord('a')]  += 1
        for j in t:
            c2[ord(j)-ord('a')]  += 1
        return sum([abs(c1[x] - c2[x]) for x in range(26)]) // 2