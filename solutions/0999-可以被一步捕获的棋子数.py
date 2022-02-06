# Problem Id:  999
# Problem Name:  Available Captures for Rook, 可以被一步捕获的棋子数
# Problem Url:  https://leetcode-cn.com/problems/available-captures-for-rook/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    xi = i
                    xj = j
                    break
        res = 0
        for i in range(xi,len(board)):
            if board[i][xj] == 'p':
                res += 1
                break
            elif board[i][xj] == 'B':
                break
        for i in range(xi,-1,-1):
            if board[i][xj] == 'p':
                res += 1
                break
            elif board[i][xj] == 'B':
                break
        for j in range(xj,len(board[0])):
            if board[xi][j] == 'p':
                res += 1
                break
            elif board[xi][j] == 'B':
                break
        for j in range(xj,-1,-1):
            if board[xi][j] == 'p':
                res += 1
                break
            elif board[xi][j] == 'B':
                break
        return res