import sys

def CheckDraw(board: list):

    filled = 0
    
    for i in board:
        for j in i:
            if not j == '?': filled = filled + 1
    
    if filled == 9: return True
    else: return False

sys.modules[__name__] = CheckDraw