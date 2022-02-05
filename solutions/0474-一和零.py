# Problem Id:  474
# Problem Name:  Ones and Zeroes, 一和零
# Problem Url:  https://leetcode-cn.com/problems/ones-and-zeroes/
# Problem Level:  Medium
 
class Solution:
    def ct(self, st: str) -> List[int]:
        length = len(st)
        m = 0
        n = 0
        for i in range(len(st)):
            if st[i] == '0':
                m = m + 1
            else:
                n = n + 1
        return [m,n]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [0] * ((m+1)*(n+1)*length)
        s = Solution().ct(strs[0])
        s0 = s[0]
        s1 = s[1]
        for j in range(m+1):
            for k in range(n+1):
                if j >= s0 and k >= s1:
                    dp[j*(n+1)+k] = 1
        for i in range(1,length):
            s = Solution().ct(strs[i])
            s0 = s[0]
            s1 = s[1]
            for j in range(m+1):
                for k in range(n+1):
                    if j - s0 < 0 or k-s1 < 0:
                        dp[i*(m+1)*(n+1)+j*(n+1)+k] = dp[(i-1)*(m+1)*(n+1)+j*(n+1)+k]
                    else:
                        dp[i*(m+1)*(n+1)+j*(n+1)+k] = max(dp[(i-1)*(m+1)*(n+1)+j*(n+1)+k],1+dp[(i-1)*(m+1)*(n+1)+(j-s0)*(n+1)+(k-s1)])
        return dp[-1]                    




        

