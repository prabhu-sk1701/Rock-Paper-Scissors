from tkinter import *
import random


window = Tk()
window.title('Rock Paper and Scissors')
window.geometry("300x300")

computer_moves = {
    '0' : 'Rock',
    '1' : 'Paper',
    '2' : 'Scissor'
}

def reset():
    b1['state'] = 'active'
    b2['state'] = 'active'
    b3['state'] = 'active'
    l1.config(text='Player          ')
    l3.config(text='Computer')
    l4.config(text='')
    
def disable_buttons():
    b1['state'] = 'disable'
    b2['state'] = 'disable'
    b3['state'] = 'disable'
    
def isrock():
    move = computer_moves[str(random.randint(0,2))]
    if move == 'Rock':
        result = 'Draw'
    elif move == 'Scissor':
        result = 'Player Wins'
    else:
        result = 'Computer Wins'
    l4.config(text=result)
    l1.config(text='Rock            ')
    l3.config(text=move)
    disable_buttons()
    
def ispaper():
    move = computer_moves[str(random.randint(0,2))]
    if move == 'Paper':
        result = 'Draw'
    elif move == 'Rock':
        result = 'Player Wins'
    else:
        result = 'Computer Wins'
    l4.config(text=result)
    l1.config(text='Paper            ')
    l3.config(text=move)
    disable_buttons()
    
def isscissor():
    move = computer_moves[str(random.randint(0,2))]
    if move == 'Scissor':
        result = 'Draw'
    elif move == 'Paper':
        result = 'Player Wins'
    else:
        result = 'Computer Wins'
    l4.config(text=result)
    l1.config(text='Scissor            ')
    l3.config(text=move)
    disable_buttons()

#GUI setup
Label(window,
      text='Rock Paper Scissors',
      font='normal 20 bold',
      fg='blue').pack(pady=20)

frame = Frame(window)
frame.pack()

l1 = Label(frame,
           text='Player         ',
           font = 10)
l2 = Label(frame,
           text='VS         ',
           font = 'normal 10 bold')
l3 = Label(frame, text='Computer', font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(window,
           text='',
           font='normal 10 bold',
           bg='white',
           width=15,
           borderwidth=2,
           relief='solid')
l4.pack(pady=20)

frame1 = Frame(window)
frame1.pack()

b1 = Button(frame1, text='Rock',
            font=10, width=7,
            command=isrock)
b2 = Button(frame1, text='Paper',
            font=10, width=7,
            command=ispaper)
b3 = Button(frame1, text='Rock',
            font=10, width=7,
            command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(window, text='Reset',
       font=10, fg='red',
       bg='black', command=reset).pack(pady=20)

window.mainloop()
