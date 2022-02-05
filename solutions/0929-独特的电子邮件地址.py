# Problem Id:  929
# Problem Name:  Unique Email Addresses, 独特的电子邮件地址
# Problem Url:  https://leetcode-cn.com/problems/unique-email-addresses/
# Problem Level:  Easy
 
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            t = emails[i].split('@')
            s = t[0]
            p = -1
            for j in range(len(s)):
                if s[j] == '+':
                    p = j
                    break
            if p != -1:
                s = s[:p]
            s = s.replace(".", "")
            emails[i] = s + '@' + t[1]
        return len(set(emails))
