# Problem Id:  72
# Problem Name:  Edit Distance, 编辑距离
# Problem Url:  https://leetcode-cn.com/problems/edit-distance/
# Problem Level:  Hard
# Language:  Python3
 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ct = {}
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        if word1[0] != word2[0]:
            ct[(0,0)] = 1
        else:
            ct[(0,0)] = 0 
        
        for j in range(1,len(word2)):
            if word2[j] == word1[0]:
                ct[(0,j)] = j
            else:
                ct[(0,j)] = ct[(0,j-1)] + 1

        for i in range(1,len(word1)):
            if word1[i] == word2[0]:
                ct[(i,0)] = i
            else:
                ct[(i,0)] = ct[(i-1,0)] + 1

        for i in range(1,len(word1)):
            for j in range(1,len(word2)):
                if word1[i] == word2[j]:
                    ct[(i,j)] = ct[(i-1,j-1)]
                else:
                    s1 = ct[(i-1,j)] + 1
                    s2 = ct[(i,j-1)] + 1
                    s3 = ct[(i-1,j-1)] + 1
                    ct[(i,j)] = min(s1,s2,s3)
        return ct[(len(word1)-1,len(word2)-1)]