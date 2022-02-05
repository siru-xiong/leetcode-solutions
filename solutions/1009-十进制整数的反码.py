# Problem Id:  1009
# Problem Name:  Complement of Base 10 Integer, 十进制整数的反码
# Problem Url:  https://leetcode-cn.com/problems/complement-of-base-10-integer/
# Problem Level:  Easy
 
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        #from math import floor
        if N == 0:
            return 1
        else:
            bit = ''
            temp = 1
            bit_temp = 0
            while True:
                if 2 * temp > N:
                    break
                else:
                    temp = temp * 2
                    bit_temp = bit_temp + 1
            while True:
                digit = floor(N / temp)
                bit = bit + str(digit)
                N = N - digit * temp
                if temp == 1:
                    break
                temp = int(temp/2)

            new_bit = ''
            for i in range(len(bit)):
                if bit[i] == '0':
                    new_bit = new_bit + '1'
                else:
                    new_bit = new_bit + '0'

            result = 0
            temp = 1
            for i in range(1,len(new_bit)+1):
                result = result + int(new_bit[-i]) * temp
                temp = temp * 2
            return result

                         