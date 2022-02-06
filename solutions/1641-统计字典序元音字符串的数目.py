# Problem Id:  1641
# Problem Name:  Count Sorted Vowel Strings, 统计字典序元音字符串的数目
# Problem Url:  https://leetcode-cn.com/problems/count-sorted-vowel-strings/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def countVowelStrings(self, n: int) -> int:
        c = [-1,1,2,3,4,5]
        for j in range(1,n):
            for i in range(5,0,-1):
                c[i] = sum(c[1:(i+1)])
        return c[-1]
        #return sum([self.countVowelStrings(n-1,i) for i in range(1,t+1)])
        
