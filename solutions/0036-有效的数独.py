# Problem Id:  36
# Problem Name:  Valid Sudoku, 有效的数独
# Problem Url:  https://leetcode-cn.com/problems/valid-sudoku/
# Problem Level:  Medium
 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = True
        for i in range(len(board)):
            t = []
            for j in board[i]:
                if j != '.':
                    t.append(j)
            result = result and len(t) == len(set(t))
        for i in range(len(board)):
            t = []
            for j in [k[i] for k in board]:
                if j != '.':
                    t.append(j)
            result = result and len(t) == len(set(t))
        for i in range(3):
            for j in range(3):
                t = []
                for k in [board[m][n] for m in range(i*3,(i+1)*3) for n in range(j*3,(j+1)*3)]:
                    if k != '.':
                        t.append(k)
                result = result and len(t) == len(set(t))
        return result