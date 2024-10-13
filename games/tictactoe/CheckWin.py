import sys

def HorizontalCheck(board: list, turn: str):
    if board[0][0] == turn and board[0][1] == turn and board[0][2] == turn:
        return True
    elif board[1][0] == turn and board[1][1] == turn and board[1][2] == turn:
        return True
    elif board[2][0] == turn and board[2][1] == turn and board[2][2] == turn:
        return True
    else: return False

def VerticalCheck(board: list, turn: str):
    if board[0][0] == turn and board[1][0] == turn and board[2][0] == turn:
        return True
    elif board[0][1] == turn and board[1][1] == turn and board[2][1] == turn:
        return True
    elif board[0][2] == turn and board[1][2] == turn and board[2][2] == turn:
        return True
    else: return False

def DiagonalCheck(board: list, turn: str):
    if board[0][0] == turn and board[1][1] == turn and board[2][2] == turn:
        return True
    elif board[0][2] == turn and board[1][1] == turn and board[2][0] == turn:
        return True
    else: return False

def CheckWin(board: list, turn: str):
    if HorizontalCheck(board, turn) or VerticalCheck(board, turn) or DiagonalCheck(board, turn): return True
    else: False

sys.modules[__name__] = CheckWin