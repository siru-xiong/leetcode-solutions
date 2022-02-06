# Problem Id:  面试题 16.02
# Problem Name:  Words Frequency LCCI, 单词频率
# Problem Url:  https://leetcode-cn.com/problems/words-frequency-lcci/
# Problem Level:  Medium
# Language:  Python3
 
class WordsFrequency:

    def __init__(self, book: List[str]):
        self.set = {}
        for i in book:
            self.set[i] = self.set.get(i,0) + 1


    def get(self, word: str) -> int:
        return self.set.get(word,0) 



# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)