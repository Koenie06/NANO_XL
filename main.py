import games.connectfour.computer.connectfour as ConnectFourComputer
import games.connectfour.user.connectfour as ConnectFourUser
import games.tictactoe.computer.tictactoe as TicTacToeComputer
import games.tictactoe.user.tictactoe as TicTacToeUser

import customtkinter
def CenterWindowToDisplay(Screen: customtkinter, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

root = customtkinter.CTk()
root.title('Simple XL Games')
# root.geometry(CenterWindowToDisplay(root, 480, 520, root._get_window_scaling()))
root.resizable(0,0)

text = customtkinter.CTkLabel(root, text=f'Simple XL Games', font=('Comic Sans MS', 35))
text.grid(row = 1, column = 0)
empty = customtkinter.CTkLabel(root, text='', font=('Comic Sans MS', 20))
empty.grid(row = 2, column = 0)

button = customtkinter.CTkButton(
    root,
    text='Connect Four',
    font=('Comic Sans MS',20),
    height = 50, width = 400, 
    corner_radius=10,
    command = lambda : ConnectFourUser())
button.grid(row = 3, column = 0, padx= 10, pady = 10)
button = customtkinter.CTkButton(
    root,
    text='Connect Four (Computer)',
    font=('Comic Sans MS',20),
    height = 50, width = 400, 
    corner_radius=10,
    command = lambda : ConnectFourUser())
button.grid(row = 4, column = 0, padx= 10, pady = 10)

button = customtkinter.CTkButton(
    root,
    text='Tic Tac Toe',
    font=('Comic Sans MS',20),
    height = 50, width = 400, 
    corner_radius=10,
    command = lambda : ConnectFourUser())
button.grid(row = 5, column = 0, padx= 10, pady = 10)
button = customtkinter.CTkButton(
    root,
    text='Tic Tac Toe (Computer)',
    font=('Comic Sans MS',20),
    height = 50, width = 400, 
    corner_radius=10,
    command = lambda : ConnectFourUser())
button.grid(row = 6, column = 0, padx= 10, pady = 10)

button = customtkinter.CTkButton(
    root,
    text='Hangman',
    font=('Comic Sans MS',20),
    height = 50, width = 400, 
    corner_radius=10,
    command = lambda : ConnectFourUser())
button.grid(row = 7, column = 0, padx= 10, pady = 10)
button = customtkinter.CTkButton(
    root,
    text='Hangman (Generated Word)',
    font=('Comic Sans MS',20),
    height = 50, width = 400, 
    corner_radius=10,
    command = lambda : ConnectFourUser())
button.grid(row = 8, column = 0, padx= 10, pady = 10)

button = customtkinter.CTkButton(
    root,
    text='Calculator',
    font=('Comic Sans MS',20),
    height = 50, width = 400, 
    corner_radius=10,
    command = lambda : ConnectFourUser())
button.grid(row = 9, column = 0, padx= 10, pady = 10)

root.mainloop()