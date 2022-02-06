# Problem Id:  412
# Problem Name:  Fizz Buzz, Fizz Buzz
# Problem Url:  https://leetcode-cn.com/problems/fizz-buzz/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        s = [str(i) for i in range(1,n+1)]
        i = 2
        while i <= n-1:
            s[i] = 'Fizz'
            i = i + 3
        j = 4
        while j <= n-1:
            if s[j] != 'Fizz':
                s[j] = 'Buzz'
            else:
                s[j] = 'FizzBuzz'
            j = j + 5
        return s
