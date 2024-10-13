import sys
turns = ['red', 'yellow']

def CheckWin(board, turn):
    for c in range(4):
        for r in range(6):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] == turns[turn]:
                return True
            
    for c in range(7):
        for r in range(3):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] == turns[turn]:
                return True
            
    for c in range(4):
        for r in range(3):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] == turns[turn]:
                return True

    for c in range(4):
        for r in range(3, 6):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] == turns[turn]:
                return True
            
    return False

sys.modules[__name__] = CheckWin