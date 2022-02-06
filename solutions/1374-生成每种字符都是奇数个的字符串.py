# Problem Id:  1374
# Problem Name:  Generate a String With Characters That Have Odd Counts, 生成每种字符都是奇数个的字符串
# Problem Url:  https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return 'a'*n
        else:
            return 'a'*(n-1)+'b'