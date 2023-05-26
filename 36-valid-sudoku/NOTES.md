class Solution:
def isValidSudoku(self, board: List[List[str]]) -> bool:
for i in range(9):
row = set()
for j in range(9):
if board[i][j] != '.' and board[i][j] in row:
return False
row.add(board[i][j])
for i in range(9):
col = set()
for j in range(9):
if board[j][i] != '.' and board[j][i] in col:
return False
col.add(board[j][i])
for k in range(9):
x = (k // 3) * 3
y = (k % 3) * 3
square = set()
for i in range(3):
for j in range(3):
if board[i+x][j+y] != '.' and board[i+x][j+y] in square:
return False
square.add(board[i+x][j+y])
return True