import sys
import customtkinter
import games.connectfour.CheckWin as CheckWin

root = customtkinter.CTk()

displayBoard = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']
]
scoreBoard = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ']
]

turns = ['red', 'yellow']
turn = 0
moves = 0
stopGame = False

def onClick(r, c):
    global moves
    global turn
    global stopGame

    if stopGame: return

    for row in range(5, -1, -1):
            if scoreBoard[row][c] == ' ':
                scoreBoard[row][c] = turns[turn]
                displayBoard[row][c].configure(fg_color=turns[turn])
                moves += 1
                break

    if CheckWin(scoreBoard, turn):
        stopGame = True
        gameText.configure(text = f'Good job {turns[turn]}! You\'ve actually won.')
        for i in range(6):
            for j in range(7):
                displayBoard[i][j].configure(hover=False)
        return
        
    turn = 0 if turn == 1 else 1
    gameText.configure(text = f'It is {turns[turn]}\'s turn')

    if moves == 42:
        stopGame = True
        for i in range(6):
            for j in range(7):
                displayBoard[i][j].configure(hover=False)
        gameText.configure(text = 'It\'s a draw!')
        return
    return

# Create the Connect Four board with round buttons and lines
canvas = customtkinter.CTkCanvas(root, width=720, height=2)  # Adjusted width to 560
canvas.create_line(0, 1, 560, 1, fill='black')
canvas.grid(row=0, column=0, columnspan=15, padx=5, pady=5)

for i in range(0, 12, 2):
    # Add horizontal lines
    canvas = customtkinter.CTkCanvas(root, width=720, height=2)  # Adjusted width to 560
    canvas.create_line(0, 1, 560, 1, fill='black')
    canvas.grid(row=i+2, column=0, columnspan=15, padx=5, pady=5)
    
    for j in range(0, 14, 2):
        # Add vertical lines
        canvas = customtkinter.CTkCanvas(root, width=2, height=75)
        canvas.create_line(1, 0, 1, 75, fill='black')
        canvas.grid(row=i+1, column=j, padx=5, pady=5)
        
        # Create round buttons
        displayBoard[int(i/2)][int(j/2)] = customtkinter.CTkButton(
            root,
            text='',
            fg_color='gray',
            font=('Comic Sans MS', 100),
            height=75, width=75,
            corner_radius=200,
            hover=False,
            state='disabled'
        )
        displayBoard[int(i/2)][int(j/2)].grid(row=i+1, column=j+1, padx=5, pady=5)

    # Add the final vertical line on the right
    canvas = customtkinter.CTkCanvas(root, width=2, height=75)
    canvas.create_line(1, 0, 1, 75, fill='black')
    canvas.grid(row=i+1, column=14, padx=5, pady=5)

# Make beneath the board another row of buttons which are clickable
for j in range(7):
    customtkinter.CTkButton(
        root,
        text='',
        font=('Comic Sans MS', 20),
        height=75, width=75,
        corner_radius=10,
        command=lambda r=6, c=j: onClick(r, c)
    ).grid(row=13, column=j*2+1, padx=5, pady=20)

gameText = customtkinter.CTkLabel(root, text = f'It is {turns[turn]}\'s turn', font=('Comic Sans MS', 30))
gameText.grid(row=14, column=0, columnspan=15)

def ConnectFour():
    root.mainloop()

sys.modules[__name__] = ConnectFour