from tkinter import *
import random


window = Tk()
window.title('Rock Paper and Scissors')
window.geometry("400x400")

computer_moves = {
    '0' : 'Rock',
    '1' : 'Paper',
    '2' : 'Scissor'
}

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
            command='''isrock''')
b2 = Button(frame1, text='Rock',
            font=10, width=7,
            command='''isrock''')
b3 = Button(frame1, text='Rock',
            font=10, width=7,
            command='''isrock''')

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(window, text='Reset',
       font=10, fg='red',
       bg='black', command='''reset_game''').pack(pady=20)

window.mainloop()
