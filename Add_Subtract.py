# Intro to Computer Programmin ITS 16163
# Module 6 Quiz
# Sidney Rood


from tkinter import*

window = Tk()
listbox = Listbox(window)


def add():
    num1 = ((int(ent1.get()))+(int(ent2.get())))
    listbox.insert(END,num1);

def sub():
    num2 = ((int(ent1.get()))-(int(ent2.get())))
    listbox.insert(END,num2);


l1 = Label(window, text="First Number: ")
l2 = Label(window, text="Second Number: ")

ent1 = Entry(window, bg = 'yellow')
ent2 = Entry(window, bg = 'light blue')

but1 = Button(window, text="Add Numbers", command = add)
but2 = Button(window, text="Subtract Numbers", command = sub)


l1.pack()
ent1.pack()
l2.pack()
ent2.pack()
but1.pack()
but2.pack()
listbox.pack()

window.mainloop()
