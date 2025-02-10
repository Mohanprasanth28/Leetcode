from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = [] 
        board = [["." for _ in range(n)] for _ in range(n)]
        self.N_queen(board, 0, n, result)
        return result

    def N_queen(self, board, col, n, result):
        if col == n:  
            result.append(["".join(row) for row in board])
            return  

        for row in range(n):
            if self.safe(board, row, col, n):
                board[row][col] = "Q"
                self.N_queen(board, col + 1, n, result)
                board[row][col] = "."  

    def safe(self, board, row, col, n):
        
        for i in range(col):
            if board[row][i] == "Q":
                return False

        
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        
        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == "Q":
                return False
            i += 1
            j -= 1

        return True
