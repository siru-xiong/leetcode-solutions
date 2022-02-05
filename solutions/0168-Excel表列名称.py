# Problem Id:  168
# Problem Name:  Excel Sheet Column Title, Excel表列名称
# Problem Url:  https://leetcode-cn.com/problems/excel-sheet-column-title/
# Problem Level:  Easy
 
class Solution:
    def convertToTitle(self, n: int) -> str:
        temp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        if n <= 26:
            return temp[n-1]
        else:
            vsum = 26
            index = 26
            length = 2
            while True:
                if vsum + index * 26 < n:
                    length = length + 1
                    vsum = vsum + index * 26
                    index = index * 26
                else:
                    break
            result = ['*'] * length
            n = n - vsum
            for i in range(length):
                result[i] = temp[(n - 1) // index]
                n = n % index
                index = index // 26
            return ''.join(result)