# Problem Id:  157
# Problem Name:  Read N Characters Given Read4, 用 Read4 读取 N 个字符
# Problem Url:  https://leetcode-cn.com/problems/read-n-characters-given-read4/
# Problem Level:  Easy
 
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        res = 0
        for i in range(0, n, 4):
            buf4 = [' '] * 4
            for j in range(read4(buf4)):
                buf[res] = buf4[j]
                res += 1
        return min(res, n)