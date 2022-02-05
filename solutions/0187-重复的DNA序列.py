# Problem Id:  187
# Problem Name:  Repeated DNA Sequences, 重复的DNA序列
# Problem Url:  https://leetcode-cn.com/problems/repeated-dna-sequences/
# Problem Level:  Medium
 
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        st = set()
        res = set()
        for i in range(len(s)-9):
            if s[i:(i+10)] in st:
                res.add(s[i:(i+10)])
            else:
                st.add(s[i:(i+10)])
        return list(res)
