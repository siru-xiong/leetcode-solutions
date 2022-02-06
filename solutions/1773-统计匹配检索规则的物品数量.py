# Problem Id:  1773
# Problem Name:  Count Items Matching a Rule, 统计匹配检索规则的物品数量
# Problem Url:  https://leetcode-cn.com/problems/count-items-matching-a-rule/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        for i in items:
            if ruleKey == 'type' and ruleValue == i[0] or ruleKey == 'color' and ruleValue == i[1] or ruleKey == 'name' and ruleValue == i[2]:
                res += 1
        return res