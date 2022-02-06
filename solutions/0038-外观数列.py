# Problem Id:  38
# Problem Name:  Count and Say, 外观数列
# Problem Url:  https://leetcode-cn.com/problems/count-and-say/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        else:
            temp = Solution().countAndSay(n - 1)
            index = 0
            count = 1
            result = ''
            for i in range(1,len(temp)):
                if temp[i] == temp[index]:
                    count = count + 1
                else:
                    result = result + str(count) + str(temp[index])
                    index = i
                    count = 1
            result = result + str(count) + str(temp[index])
            return result