from tkinter import *
from tkinter import messagebox
import subprocess
import os
import sys


container = Tk()


def about():
        #About
        messagebox.showinfo("About", "MesShow means Message Show.This software is coded by Vyankatesh Pipalwa")


def how():
        #How to
        messagebox.showinfo("How to use","Type username or usernames in User Names box and type any message in Message box and click execute. Press Clear to clear data of text field.")


def compati():
        #Compatibility
        messagebox.showinfo("Compatibility","This software is compatible with Windows XP, Windows 7, Windows 8, Windows 8.1, Windows 10 Pro, Windows Server(All) and not compatible with Windows 11 and Windows 10 Home. I am working on that.")


def delTextBox():
        #Delete
        userText.delete("1.0", "end")
        messageText.delete("1.0", "end")


def show():
        #Delivered message
        messagebox.showinfo("Done","Message has been delivered.")


def process():
        #To get input from text box
        items1 = userText.get('1.0','end')
        items2 = messageText.get('1.0','end')
        #Adding usernames in list
        lst1 = [item for item in items1.split()]
        if len(items1) == 1:
                #Checking that username box is empty or filled
                messagebox.showwarning("Warning", "Please enter username/usernames in the field!")
        
        elif len(items2) == 1: 
                #Checking that message box is empty or filled
                messagebox.showwarning("Warning", "Please enter message in the field!")

        else:
                #Running CMD command 
                for lists in lst1:
                        subprocess.call(f"msg {lists} {items2}")
                show()
                delTextBox()
        

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


#Title
container.title("MesShow")
#Width X Height
container.geometry("710x500")
#Background color
container.config(bg="lightgreen")
#Icon
iconPath = resource_path("logoV2.ico")
container.iconbitmap(iconPath)


#Username label
userLabel = Label(container, text='User Names :', bg="lightgreen", font=("Helvetica", "12", "bold"))
userLabel.grid(row=0, column=1, padx=25, pady=25)
#Text box
userText = Text(container, width=30, height=18)
userText.grid(row=1, column=1, padx=25)


#Message label
messageLabel = Label(container, text='Message :', bg="lightgreen", font=("Helvetica", "12", "bold"))
messageLabel.grid(row=0, column=2, padx=25, pady=25)
#Text box
messageText = Text(container, width=45, height=18)
messageText.grid(row=1, column=2, padx=25)


#Clear button
clearButton = Button(container, text='Clear', width=10, activebackground='#8af', command=delTextBox)
clearButton.grid(row=2, column=2, padx=25, pady=50)
#Execute button
executeButton = Button(container, text='Execute', width=20, activebackground='#8af', command=process)
executeButton.grid(row=2, column=1, padx=25, pady=50)


#Menu section
menu = Menu(container)
container.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=container.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Compatibility', command=compati)
helpmenu.add_command(label='How', command=how)
helpmenu.add_command(label='About', command=about)
#Loop
container.mainloop()