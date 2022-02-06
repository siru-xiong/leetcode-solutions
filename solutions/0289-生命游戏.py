# Problem Id:  289
# Problem Name:  Game of Life, 生命游戏
# Problem Url:  https://leetcode-cn.com/problems/game-of-life/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        p = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                q = 0
                r = [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
                for k in r:
                    if k[0] >= 0 and k[0] < len(board) and k[1] >= 0 and k[1] < len(board[0]):
                        if board[k[0]][k[1]] == 1:
                            q = q + 1
                if board[i][j] == 0 and q == 3:
                    p.append([i,j])
                elif board[i][j] == 1 and (q < 2 or q > 3):
                    p.append([i,j])
        for i in p:
            board[i[0]][i[1]] = 1 - board[i[0]][i[1]]
        return board
                        
                
