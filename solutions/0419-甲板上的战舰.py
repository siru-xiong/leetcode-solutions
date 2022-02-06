# Problem Id:  419
# Problem Name:  Battleships in a Board, 甲板上的战舰
# Problem Url:  https://leetcode-cn.com/problems/battleships-in-a-board/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    if j == 0 or board[i][j-1] == '.':
                        if i == 0 or board[i-1][j] == '.':
                            res = res + 1
        return res
                
