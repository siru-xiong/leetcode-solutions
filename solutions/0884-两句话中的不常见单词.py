# Problem Id:  884
# Problem Name:  Uncommon Words from Two Sentences, 两句话中的不常见单词
# Problem Url:  https://leetcode-cn.com/problems/uncommon-words-from-two-sentences/
# Problem Level:  Easy
 
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split(' ')
        B = B.split(' ')
        counta = {}
        countb = {}
        for i in range(len(A)):
            counta[A[i]] = counta.get(A[i],0) + 1
        for j in range(len(B)):
            countb[B[j]] = countb.get(B[j],0) + 1
        result = []
        for i in range(len(A)):
            if counta[A[i]] == 1 and A[i] not in countb:
                result.append(A[i])
        for j in range(len(B)):
            if countb[B[j]] == 1 and B[j] not in counta:
                result.append(B[j])
        return result
