# Problem Id:  面试题 05.03
# Problem Name:  Reverse Bits LCCI, 翻转数位
# Problem Url:  https://leetcode-cn.com/problems/reverse-bits-lcci/
# Problem Level:  Easy
 
class Solution:
    def reverseBits(self, num: int) -> int:
        neg = 0
        if num == -1:
            return 32
        if num < 0:
            neg = 1
            num = -num - 1
        elif num == 0:
            return 1
        elif num == 1:
            return 2
        i = []
        base = 0
        t = 1
        while t*2 <= num:
            t *= 2
            base + 1
        while t != 0:
            i.append(num//t)
            num = num - t*(num//t)
            t //= 2
        r = 1
        if neg == 1:
            y = [1-x for x in i]
            i = [1] * (32-len(y)) + y
            la = -1
            
        while True:
            if i[r] == 1:
                if i[r-1] >= 1:
                    i[r-1] += 1
                    del i[r]
                else:
                    r += 1
            else:
                r += 1
            if r == len(i):
                break
        if neg == 0:
            i = [0] + i
        print(i)
        res = max(i) + 1
        if len(i) == 1:
            return res
        for j in range(len(i)):
            if j == 0:
                if i[j] == 0 and i[j+1] > 0:
                    res = max(res,i[j+1]+1)
            elif j == len(i)-1:
                if i[j] == 0 and i[j-1] > 0:
                    res = max(res,i[j-1]+1)
            else:
                if i[j] == 0 and i[j+1] > 0 and i[j-1] > 0:
                    res = max(res,i[j-1]+i[j+1]+1)
        return res

