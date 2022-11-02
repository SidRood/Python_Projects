# Intro to Computer Programming ITS 16163
# Final - Bear Daycare
# Sidney Rood


from tkinter import *

#creat the window and listbox
window = Tk()
listbox = Listbox(window)


#using class and definition with the objects we will call on
#using definition and if else to navigate through the actisvities the user chooses

def name():
    ww = (ent1.get())
    w7 = ("Grrrrrr, I'm your new bear!")
    listbox.insert(END,ww);
    listbox.insert(END,w7);

def mood():
    w1 = ("I feel grrrreeaattt right now.\n")
    listbox.insert(END,w1);
    
def eat():
    w2 = ("Arrrr Yummy. Thank you.")
    listbox.insert(END,w2);

def play():
    w3 = ("Yay! Rawr...grrrrr, Lets go!")
    listbox.insert(END,w3);

def cuddle():
    w4 = ("Awww, I love you beary much!")
    listbox.insert(END,w4);

def nap():
    w6 = ("Rawrrrr, time to hibernate.")
    listbox.insert(END,w6);

def quit_():
    w8 = ("Bye, Bye, see you tommorow!")
    listbox.insert(END,w8);


    

#create labels for the GUI window to direct the user
l1 = Label(window, text="Welcome to Bear Daycare!!!")
l2 = Label(window, text=''' ____
                        ┈╭━╱▔▔▔▔╲━╮┈┈┈
                        ┈┈╰╱╭▅╮╭▅╮╲╯┈┈┈
                        ╳┈┈▏╰┈▅▅┈╯▕┈┈┈┈
                        ┈┈┈╲┈╰━╯┈╱┈┈╳┈
                        ┈┈┈╱╱▔╲╱▔╲╲┈┈┈┈
                        ┈╭━╮▏┊┊▕▔╭━╮┈╳
                        ┈┃┊┣╲┊┊╱┫┊┃┈┈
                        ┈╰━━╲╱━━╯┈╳''')                                                   

l3 = Label(window, text="What do you want to name your new bear?: ")
l4 = Label(window, text='''
Bear Activities:
1 - Find your bears mood
2 - Play with your bear
3 - Feed your bear
4 - Cuddle with your bear
6 - Nap time for your bear
7 - Quit

Enter the Activity you want to do:''')
           
#create entry box for name
ent1 = Entry(window)

#create buttons for activities
buta = Button(window, bg ='yellow', text="Enter Name", command = name)
but1 = Button(window, bg ='orange', text="1", command = mood)
but2 = Button(window, bg ='red', text="2", command = play)
but3 = Button(window, bg ='pink', text="3", command = eat)
but4 = Button(window, bg ='purple', text="4", command = cuddle)
but6 = Button(window, bg ='blue', text="6", command = nap)
but7 = Button(window, bg ='green', text="7", command = quit_)

#pack all the labels, entry boxes, buttons, and the listbox into the window
l1.pack()
l2.pack()
l3.pack()
ent1.pack()
buta.pack()
l4.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()
but6.pack()
but7.pack()
listbox.pack()
listbox.config(width=50,height=10)


window.mainloop()





'''make the mood random; make title; global command; can you grid?'''

