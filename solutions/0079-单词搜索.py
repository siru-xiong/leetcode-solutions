# Problem Id:  79
# Problem Name:  Word Search, 单词搜索
# Problem Url:  https://leetcode-cn.com/problems/word-search/
# Problem Level:  Medium
 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def es(bd, word, start, used):
            if len(word) == 1:
                re = False
                temp = [[start[0]-1,start[1]],[start[0]+1,start[1]],[start[0],start[1]-1],[start[0],start[1]+1]]
                for j in temp:
                    if j[0] >= 0 and j[0] < len(bd) and j[1] >= 0 and j[1] < len(bd[0]):
                        if tuple(j) not in used:
                            if bd[j[0]][j[1]] ==  word:
                                re = True
                return re                
            else:
                re = False
                temp = [[start[0]-1,start[1]],[start[0]+1,start[1]],[start[0],start[1]-1],[start[0],start[1]+1]]
                for j in temp:
                    if j[0] >= 0 and j[0] < len(bd) and j[1] >= 0 and j[1] < len(bd[0]):
                        if tuple(j) not in used:
                            if bd[j[0]][j[1]] == word[0]:
                                used.add((j[0],j[1]))
                                re = re or es(bd,word[1:],[j[0],j[1]],used)
                                used.remove((j[0],j[1]))
                return re
        result = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    else:
                        result = result or es(board,word[1:],[i,j],set([(i,j)]))
        return result

