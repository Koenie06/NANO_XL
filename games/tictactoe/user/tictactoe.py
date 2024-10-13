import sys
from tkinter import *
import customtkinter
import games.tictactoe.CheckWin as CheckWin
import games.tictactoe.CheckDraw as CheckDraw

def CenterWindowToDisplay(Screen: customtkinter, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

root = customtkinter.CTk()
root.title('TicTacToe')
root.geometry(CenterWindowToDisplay(root, 480, 520, root._get_window_scaling()))
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
turn = 0
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
        gameText.configure(text = f'Good job {turns[turn]}! You\'ve actually won.')
        return
    elif CheckDraw(scoreBoard) == True:
        gameText.configure(text = 'It\'s a draw!')
        stopGame = True
        for i in range(3):
            for j in range(3):
                displayBoard[i][j].configure(hover=False)
        return
    
    turn = 0 if turn == 1 else 1
    gameText.configure(text = f'It is {turns[turn]}\'s turn')
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

# Add a text to display the winner
gameText = customtkinter.CTkLabel(root, text=f'It is {turns[turn]}\'s turn', font=('Comic Sans MS', 20))
gameText.grid(row = 3, column = 0, columnspan = 3)

def TicTacToe():
    root.mainloop()

sys.modules[__name__] = TicTacToe