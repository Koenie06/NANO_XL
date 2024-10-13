import sys, math
from tkinter import *
import customtkinter

def CenterWindowToDisplay(Screen: customtkinter, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

root = customtkinter.CTk()
root.title('Calculator')
# root.geometry(CenterWindowToDisplay(root, 480, 520, root._get_window_scaling()))
root.resizable(0,0)

calculatorBoard = [
    ['e', 'x!', '(', ')', '%', 'CE'],
    ['sin', 'π', '7', '8', '9', '÷'],
    ['cos', 'log', '4', '5', '6', 'x'],
    ['tan', '√', '1', '2', '3', '-'],
    ['ans', 'xʸ', '.', '0', '=', '+']
]
calculatorButtons = [
    ['e', 'x!', '(', ')', '%', 'CE'],
    ['sin', 'π', '7', '8', '9', '÷'],
    ['cos', 'log', '4', '5', '6', 'x'],
    ['tan', '√', '1', '2', '3', '-'],
    ['ans', 'xʸ', '.', '0', '=', '+']
]
superscript_map = {
    '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵',
    '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', 
    '+': '⁺', '-': '⁻', '=': '⁼', '(': '⁽', ')': '⁾',
    'a': 'ᵃ', 'b': 'ᵇ', 'c': 'ᶜ', 'd': 'ᵈ', 'e': 'ᵉ', 'f': 'ᶠ', 
    'g': 'ᵍ', 'h': 'ʰ', 'i': 'ⁱ', 'j': 'ʲ', 'k': 'ᵏ', 'l': 'ˡ',
    'm': 'ᵐ', 'n': 'ⁿ', 'o': 'ᵒ', 'p': 'ᵖ', 'r': 'ʳ',
    's': 'ˢ', 't': 'ᵗ', 'u': 'ᵘ', 'v': 'ᵛ', 'w': 'ʷ', 'x': 'ˣ',
    'y': 'ʸ', 'z': 'ᶻ',
}

stopGame = False
calculatorListbg = ['0']
calculatorAnswer = '0'
bracketActive = []
powerActive = False

def getButtonText(calcList):
    if len(calcList) == 0: return ['0']
    def checkUpper(x):
        if x == 'ʸ':
            return ''
        if x.__contains__('^'):
            x = x.replace('^', '')
            return superscript_map[x]
        return x
    return list(map(checkUpper, calcList))

def onClick(r,c):
    global stopGame
    global calculatorListbg
    global calculatorAnswer
    global bracketActive
    global powerActive

    if stopGame: return

    if calculatorBoard[r][c] == 'CE':
        calculatorListbg = ['0']
        answerLabel.configure(text='                                          ................')
        backgroundButton.configure(text='0')
        powerActive = False
        return
    
    if calculatorBoard[r][c] == 'ans':
        if not len(calculatorListbg) == 0:
            if calculatorListbg[-1] not in ['+', '-', 'x', '÷', '(']:
                calculatorListbg.append('x')
            if calculatorListbg[-1] not in ['^+', '^-', '^x', '^÷', '^(']:
                calculatorListbg.append('^x')
        if powerActive:
            calculatorListbg.append('^', calculatorAnswer)
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        calculatorListbg.append(calculatorAnswer)
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        if calculatorListbg[-1] == '.':
            calculatorListbg.append(calculatorBoard[r][c])
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        if calculatorListbg[-1] == '^.':
            calculatorListbg.append('^' + calculatorBoard[r][c])
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        if calculatorListbg == ['0']:
            calculatorListbg = []
        if not len(calculatorListbg) == 0:
            if calculatorListbg[-1] not in ['+', '-', 'x', '÷', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', 'ʸ'] and calculatorListbg[-1] not in ['^+', '^-', '^x', '^÷', '^1', '^2', '^3', '^4', '^5', '^6', '^7', '^8', '^9', '^0', '^(', 'ʸ']:
                if calculatorListbg[-1] not in ['+', '-', 'x', '÷', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', 'ʸ']:
                    calculatorListbg.append('x')
                else:
                    calculatorListbg.append('^x')
        if powerActive:
            calculatorListbg.append('^' + calculatorBoard[r][c])
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        calculatorListbg.append(calculatorBoard[r][c])
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] in ['+', 'x', '÷']:
        if calculatorBoard[r][c] == '÷' and powerActive:
            powerActive = False
        if calculatorListbg[-1] == '.':
            calculatorListbg.append('0')
        if calculatorListbg[-1] == '^.':
            calculatorListbg.append('^0')
        if calculatorListbg == 0 or calculatorListbg[-1] in ['+', '-', 'x', '÷', '(']: return
        if calculatorListbg == 0 or calculatorListbg[-1] in ['^+', '^-', '^x', '^÷', '^(']: return
        if powerActive:
            calculatorListbg.append('^' + calculatorBoard[r][c])
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        calculatorListbg.append(calculatorBoard[r][c])
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == '-':
        if calculatorListbg[-1] == '-' or calculatorListbg[-1] == '^-': return
        if ''.join(getButtonText(calculatorListbg)) == '0':
            calculatorListbg = ['-']
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        if powerActive:
            calculatorListbg.append('^-')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        calculatorListbg.append('-')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == '.':
        if not len(calculatorListbg) == 0:
            if calculatorListbg[-1] not in ['+', '-', 'x', '÷', '%', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                calculatorListbg.append('x')
        if calculatorListbg[-1] in ['+', '-', 'x', '÷']:
            calculatorListbg.append('0')
        if calculatorListbg[-1] in ['^+', '^-', '^x', '^÷']:
            calculatorListbg.append('^0')
        if powerActive:
            calculatorListbg.append('^.')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        calculatorListbg.append('.')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == '%':
        if powerActive:
            powerActive = False
        if calculatorListbg[-1] in ['+', '-', 'x', '÷', '(']:
            calculatorListbg.append('0')
        if calculatorListbg[-1] in ['^+', '^-', '^x', '^÷']:
            calculatorListbg.append('0')
        calculatorListbg.append('%')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == 'x!':
        if powerActive:
            powerActive = False
        if calculatorListbg[-1] in ['+', '-', 'x', '÷']:
            calculatorListbg.append('0')
        if calculatorListbg[-1] in ['^+', '^-', '^x', '^÷']:
            calculatorListbg.append('0')
        calculatorListbg.append('!')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == 'π':
        if powerActive:
            powerActive = False
        if ''.join(getButtonText(calculatorListbg)) == '0':
            calculatorListbg = ['π']
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        if calculatorListbg[-1] in ['+', '-', 'x', '÷', '%']:
            calculatorListbg.append('x')
        if calculatorListbg[-1] in ['^+', '^-', '^x', '^÷']:
            calculatorListbg.append('^x')
        calculatorListbg.append('π')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == 'e':
        if ''.join(getButtonText(calculatorListbg)) == '0':
            calculatorListbg = ['e']
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        if powerActive:
            calculatorListbg.append('^e')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        calculatorListbg.append('e')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == 'sin':
        if ''.join(getButtonText(calculatorListbg)) == '0':
            calculatorListbg = ['sin']
            calculatorListbg.append('(')
            bracketActive.append('True')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        if calculatorListbg[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'π', 'e', ')', '%', '!']:
            calculatorListbg.append('x')
        if calculatorListbg[-1] in ['^1', '^2', '^3', '^4', '^5', '^6', '^7', '^8', '^9', '^0', '^e', '^)']:
            calculatorListbg.append('^x')
        if powerActive:
            calculatorListbg.append('^sin')
            calculatorListbg.append('^(')
            bracketActive.append('^True')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        calculatorListbg.append('sin')
        calculatorListbg.append('(')
        bracketActive.append('True')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == 'cos':
        if ''.join(getButtonText(calculatorListbg)) == '0':
            calculatorListbg = ['cos']
            calculatorListbg.append('(')
            bracketActive.append('True')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        if calculatorListbg[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'π', 'e', ')', '%', '!']:
            calculatorListbg.append('x')
        if calculatorListbg[-1] in ['^1', '^2', '^3', '^4', '^5', '^6', '^7', '^8', '^9', '^0', '^e', '^)']:
            calculatorListbg.append('^x')
        if powerActive:
            calculatorListbg.append('^cos')
            calculatorListbg.append('^(')
            bracketActive.append('^True')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        calculatorListbg.append('cos')
        calculatorListbg.append('(')
        bracketActive.append('True')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == 'tan':
        if ''.join(getButtonText(calculatorListbg)) == '0':
            calculatorListbg = ['tan']
            calculatorListbg.append('(')
            bracketActive.append('True')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        if calculatorListbg[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'π', 'e', ')', '%', '!']:
            calculatorListbg.append('x')
        if calculatorListbg[-1] in ['^1', '^2', '^3', '^4', '^5', '^6', '^7', '^8', '^9', '^0', '^e', '^)']:
            calculatorListbg.append('^x')
        if powerActive:
            calculatorListbg.append('^tan')
            calculatorListbg.append('^(')
            bracketActive.append('^True')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        calculatorListbg.append('tan')
        calculatorListbg.append('(')
        bracketActive.append('True')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == 'log':
        if ''.join(getButtonText(calculatorListbg)) == '0':
            calculatorListbg = ['log']
            calculatorListbg.append('(')
            bracketActive.append('True')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        if calculatorListbg[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'π', 'e', ')', '%', '!']:
            calculatorListbg.append('x')
        if calculatorListbg[-1] in ['^1', '^2', '^3', '^4', '^5', '^6', '^7', '^8', '^9', '^0', '^e', '^)']:
            calculatorListbg.append('^x')
        if powerActive:
            calculatorListbg.append('^log')
            calculatorListbg.append('^(')
            bracketActive.append('^True')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        calculatorListbg.append('log')
        calculatorListbg.append('(')
        bracketActive.append('True')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == '√':
        if powerActive:
            powerActive = False
        if ''.join(getButtonText(calculatorListbg)) == '0':
            calculatorListbg = ['√']
            calculatorListbg.append('(')
            bracketActive.append('True')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        if calculatorListbg[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'π', 'e', ')', '%', '!']:
            calculatorListbg.append('x')
        if calculatorListbg[-1] in ['^1', '^2', '^3', '^4', '^5', '^6', '^7', '^8', '^9', '^0', '^e', '^)']:
            calculatorListbg.append('x')
        calculatorListbg.append('√')
        calculatorListbg.append('(')
        bracketActive.append('True')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == '(':
        if calculatorListbg[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'π', 'e', ')', '%', '!']:
            calculatorListbg.append('x')
        if calculatorListbg[-1] in ['^1', '^2', '^3', '^4', '^5', '^6', '^7', '^8', '^9', '^0', '^e', '^)']:
            calculatorListbg.append('^x')
        if powerActive:
            calculatorListbg.append('^(')
            bracketActive.append('^True')
            backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            return
        calculatorListbg.append('(')
        bracketActive.append('True')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        return
    
    if calculatorBoard[r][c] == ')':
        if len(bracketActive) > 0:
            if bracketActive[0] == '^True':
                calculatorListbg.append(')')
                bracketActive.pop(0)
                backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
                return
            elif bracketActive[0] == 'True':
                calculatorListbg.append(')')
                bracketActive.pop(0)
                backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
            elif bracketActive[0] == '^^True':
                bracketActive.pop(0)
                powerActive = False
                backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        else: return
    
    if calculatorBoard[r][c] == 'xʸ':
        if powerActive: return
        calculatorListbg.append('ʸ')
        backgroundButton.configure(text=''.join(getButtonText(calculatorListbg)))
        powerActive = True
        return


backgroundButton = customtkinter.CTkButton(
    root,
    text='0',
    font=('Comic Sans MS',50),
    fg_color='#313131',
    height= 200, width = 570,
    corner_radius=40,
    hover=False
)
backgroundButton.grid(row = 0, column = 0, columnspan = 6, rowspan = 4, padx= 5, pady = 5)
answerLabel = customtkinter.CTkLabel(
    root,
    bg_color='#313131',
    font=('Comic Sans MS',30),
    text='                                          ................',
)
answerLabel.grid(row = 3, column = 0, columnspan = 6)

emptyLabel = customtkinter.CTkLabel(
    root,
    text='',
)
emptyLabel.grid(row = 5, column = 0, columnspan = 6)
emptyLabel = customtkinter.CTkLabel(
    root,
    text='',
)
emptyLabel.grid(row = 4, column = 0, columnspan = 6)
emptyLabel = customtkinter.CTkLabel(
    root,
    text='',
)
emptyLabel.grid(row = 0, column = 0, columnspan = 6)


for i in range(5):
    for j in range(6):
        if calculatorBoard[i][j] in ['.','0','1','2','3','4','5','6','7','8','9']:
            calculatorButtons[i][j] = customtkinter.CTkButton(
                root,
                text=calculatorBoard[i][j],
                fg_color='#383737',
                hover_color='#292828',
                font=('Comic Sans MS',40),
                height = 85, width = 85, 
                corner_radius=10,
                command = lambda r = i, c = j : onClick(r,c))
            calculatorButtons[i][j].grid(row = i+6, column = j, padx= 5, pady = 5)
            continue
        if calculatorBoard[i][j] == '=':
            calculatorButtons[i][j] = customtkinter.CTkButton(
                root,
                text=calculatorBoard[i][j],
                fg_color='#016fa1',
                hover_color='#005983',
                font=('Comic Sans MS',40),
                height = 85, width = 85, 
                corner_radius=10,
                command = lambda r = i, c = j : onClick(r,c))
            calculatorButtons[i][j].grid(row = i+6, column = j, padx= 5, pady = 5)
            continue
        calculatorButtons[i][j] = customtkinter.CTkButton(
                        root,
                        text=calculatorBoard[i][j],
                        fg_color='#616161',
                        hover_color='#4d4d4d',
                        font=('Comic Sans MS',40),
                        height = 85, width = 85, 
                        corner_radius=10,
                        command = lambda r = i, c = j : onClick(r,c))
        calculatorButtons[i][j].grid(row = i+6, column = j, padx= 5, pady = 5)

def Calculator():
    root.mainloop()

Calculator()

sys.modules[__name__] = Calculator