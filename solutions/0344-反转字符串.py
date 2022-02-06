# Problem Id:  344
# Problem Name:  Reverse String, 反转字符串
# Problem Url:  https://leetcode-cn.com/problems/reverse-string/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) >= 2:
            i = 0
            j = len(s)-1
            while True:
                s[i],s[j] = s[j],s[i]
                i,j = i+1,j-1
                if j - i == 1:
                    s[i],s[j] = s[j],s[i]
                    break
                if i - j >= 0:
                    break

            
