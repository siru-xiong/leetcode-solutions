# Problem Id:  811
# Problem Name:  Subdomain Visit Count, 子域名访问计数
# Problem Url:  https://leetcode-cn.com/problems/subdomain-visit-count/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        for i in range(len(cpdomains)):
            website = cpdomains[i].split(' ')
            num = int(website[0])
            website = website[1].split('.')
            for j in range(len(website)):
                temp = ".".join(website[j:])
                count[temp] = count.get(temp,0) + num
        result = []
        keys = list(count.keys())
        values = list(count.values())
        for i in range(len(count)):
            result.append(str(values[i])+' '+keys[i])
        return result
