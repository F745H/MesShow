from tkinter import *
from tkinter import messagebox
import subprocess

container = Tk()

def venky():
        #Coded by
        messagebox.showinfo("Coded By", "MesShow means Message Show.This software is coded by Vyankatesh Pipalwa")

def how():
        #How to
        messagebox.showinfo("How to use","Type username or usernames in User Names box and type any message in Message box and click execute. Press Clear to clear data of text field.")

def compati():
        #Compatibility
        messagebox.showinfo("Compatibility","This software is compatible with Windows XP, Windows 7, Windows 8, Windows 8.1, Windows 10 Pro, Windows Server(All) and not compatible with Windows 11 and Windows 10 Home. I am working on that.")

def delete():
        #Delete
        my_text.delete("1.0", "end")
        my_text2.delete("1.0", "end")

def show():
        #Delivered message
        messagebox.showinfo("Done","Message has been delivered.")

def process():
        #To get input from text box
        items1 = my_text.get('1.0','end')
        items2 = my_text2.get('1.0','end')
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
                delete()
        
#Title
container.title("MesShow")
#Width X Length
container.geometry("710x500")
#Background color
container.config(bg="lightgreen")
#Icon
container.iconbitmap('D:\PycharmProjects\Exit_Message\logoV2.ico')

#Username label
user_label = Label(container, text='User Names :', bg="lightgreen", font=("Helvetica", "12", "bold"))
user_label.grid(row=0, column=1, padx=25, pady=25)
#Text box
my_text = Text(container, width=30, height=18)
my_text.grid(row=1, column=1, padx=25)

#Message label
user_label2 = Label(container, text='Message :', bg="lightgreen", font=("Helvetica", "12", "bold"))
user_label2.grid(row=0, column=2, padx=25, pady=25)
#Text box
my_text2 = Text(container, width=45, height=18)
my_text2.grid(row=1, column=2, padx=25)

#Clear button
button1= Button(container, text='Clear', width=10, activebackground='#8af', command=delete)
button1.grid(row=2, column=1, padx=25, pady=50)

#Execute button
button2= Button(container, text='Execute', width=20, activebackground='#8af', command=process)
button2.grid(row=2, column=2, padx=25, pady=50)

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
helpmenu.add_command(label='About', command=venky)
#Loop
container.mainloop()