import random
import sys
from tkinter import *
import customtkinter
import games.tictactoe.CheckWin as CheckWin
import games.tictactoe.CheckDraw as CheckDraw
import games.tictactoe.computer.GetComputerMove as GetComputerMove

def CenterWindowToDisplay(Screen: customtkinter, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

root = customtkinter.CTk()
root.title('TicTacToe')
root.geometry(CenterWindowToDisplay(root, 480, 550, root._get_window_scaling()))
root.resizable(0,0)

displayBoard = [
    ['?', '?', '?'],
    ['?', '?', '?'],
    ['?', '?', '?']
]
scoreBoard = [
    ['?', '?', '?'],
    ['?', '?', '?'],
    ['?', '?', '?']
]

turns = ['X', 'O']
turn = random.randint(0,1)
stopGame = False

def onClick(r,c):
    global turn
    global stopGame

    if stopGame: return
    if scoreBoard[r][c] != '?': return
    displayBoard[r][c].configure(text = turns[turn], text_color='black')
    scoreBoard[r][c] = turns[turn]

    if CheckWin(scoreBoard, turns[turn]) == True:
        stopGame = True
        for i in range(3):
            for j in range(3):
                displayBoard[i][j].configure(hover=False)
        if turn == 0:
            gameText.configure(text = f'Wow, good job {turns[0]}!\nYou won agains the computer.')
        else:
            gameText.configure(text = f'Nice try..\nbut the computer ({turns[1]}) won.')
        return
    elif CheckDraw(scoreBoard) == True:
        gameText.configure(text = 'What??\nIt ended in a draw..')
        stopGame = True
        for i in range(3):
            for j in range(3):
                displayBoard[i][j].configure(hover=False)
        return
    
    turn = 0 if turn == 1 else 1

    move = GetComputerMove(scoreBoard)
    scoreBoard[move[0]][move[1]] = turns[1]
    displayBoard[move[0]][move[1]].configure(text = turns[1], text_color='black')

    if CheckWin(scoreBoard, turns[turn]) == True:
        stopGame = True
        for i in range(3):
            for j in range(3):
                displayBoard[i][j].configure(hover=False)
        if turn == 0:
            gameText.configure(text = f'Wow, good job {turns[0]}!\nYou won agains the computer.')
        else:
            gameText.configure(text = f'Nice try..\nbut the computer ({turns[1]}) won.')
        return
    elif CheckDraw(scoreBoard) == True:
        gameText.configure(text = 'What??\nIt ended in a draw..')
        stopGame = True
        for i in range(3):
            for j in range(3):
                displayBoard[i][j].configure(hover=False)
        return

    turn = 1 if turn == 0 else 0

    gameText.configure(text = f'The computer is waiting for you..\nHurry up!')
    return

for i in range(3):
    for j in range(3):                          
        displayBoard[i][j] = customtkinter.CTkButton(
                        root,
                        text='',
                        font=('Comic Sans MS',100),
                        height = 150, width = 150, 
                        corner_radius=10,
                        command = lambda r = i, c = j : onClick(r,c))
        displayBoard[i][j].grid(row = i, column = j, padx= 5, pady = 5)

if turn == 1:
    move = GetComputerMove(scoreBoard)
    scoreBoard[move[0]][move[1]] = turns[1]
    displayBoard[move[0]][move[1]].configure(text = turns[1], text_color='black')
    turn = 0

gameText = customtkinter.CTkLabel(root, text=f'The computer is waiting for you..\nHurry up!', font=('Comic Sans MS', 20))
gameText.grid(row = 3, column = 0, columnspan = 3)

def TicTacToe():
    root.mainloop()

sys.modules[__name__] = TicTacToe