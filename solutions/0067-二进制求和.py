# Problem Id:  67
# Problem Name:  Add Binary, 二进制求和
# Problem Url:  https://leetcode-cn.com/problems/add-binary/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a ,b = b, a
        a = list(a)
        b = list(b)
        i = -1
        index = 0
        while i >= -len(b):
            if index == 1:
                if a[i] == '0' and b[i] == '0':
                    a[i] = '1'
                    index = 0
                elif a[i] == '1' and b[i] == '1':
                    a[i] = '1'
                    index = 1
                else:
                    a[i] = '0'
                    index = 1
                i = i -1
            else:
                if a[i] == '0' and b[i] == '0':
                    a[i] = '0'
                elif a[i] == '1' and b[i] == '1':
                    a[i] = '0'
                    index = 1
                else:
                    a[i] = '1'
                i = i -1
        while i >= -len(a):
            if index == 1:
                if a[i] == '0':
                    index = 0
                    a[i] = '1'
                    break
                else:
                    a[i] = '0'
                    index = 1
                i = i - 1
            else:
                break
        if index == 1:
            return ''.join(['1']+a)
        else:
            return ''.join(a)
        
