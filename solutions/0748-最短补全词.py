# Problem Id:  748
# Problem Name:  Shortest Completing Word, 最短补全词
# Problem Url:  https://leetcode-cn.com/problems/shortest-completing-word/
# Problem Level:  Easy
 
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        import copy
        count = {}
        for i in range(len(licensePlate)):
            if licensePlate[i].isalpha():
                count[licensePlate[i].lower()] = count.get(licensePlate[i].lower(),0)+1
        length = float('inf')
        for word in words:
            ct = {}
            index = True
            for i in range(len(word)):
                if word[i] in count:
                    ct[word[i]] = ct.get(word[i],0) + 1
            for i in count.keys():
                if i not in ct or ct[i] < count[i]:
                    index = False
                    break
            if index == True and len(word) < length:
                length = len(word)
                result = word
        return result

        