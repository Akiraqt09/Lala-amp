#Simple banking system
from tkinter import *
from tkinter import messagebox

def deposit():
    if not entry.get().isnumeric():
        actions.config(text="Invalid Input!", fg="red")
        messagebox.showerror(title=
                                "Error!!", message=
                                "Invalid Input!!")
        return
    global balance
    balance += int(entry.get())
    display_balance.config(text=(f"Balance: ₱{balance}"))
    actions.config(text=(f"You've deposit: ₱{entry.get()}"), fg="green")
    
    
def withdraw():
    if not entry.get().isnumeric():
        messagebox.showerror(title=
                                "Error!!", message=
                                "Invalid Input!!")
        actions.config(text="Invalid Input!", fg="red")
        return
    global balance
    if balance < int(entry.get()):
        actions.config(text="Not enough balance!!", fg="red")
        return
    balance -= int(entry.get())
    display_balance.config(text=(f"Balance: ₱{balance}"))
    actions.config(text=(f"You've withdrawn: ₱{entry.get()}"), fg="green")
    
       
window = Tk()

balance = 0

window.config(bg="black")
#Title
title = Label(window,
                       text="Simple Banking",
                       font=("Arial", 20, "bold"),
                       fg="White",
                       bg="black")
title.pack()

#Space
label = Label(window, text="A",bg="black")
label.pack()

#Show actions
actions = Label(window,
                         text="Welcome, dear user",
                            font=("Arial",10,"bold"),
                            fg="white",
                            bg="black")
actions.pack()

#Balance
display_balance = Label(window,
                       text=(f"Balance: ₱{balance}"),
                       font=("Arial", 10, "bold"),
                       fg="White",
                       bg="black")
display_balance.pack()

#Entry
entry = Entry()
entry.config(bg="white",
                       font=("Arial",10))
entry.pack()

#Deposit
deposit_button = Button(window,
                                text="Deposit",
                                font=("Arial",10),
                                command=deposit)
deposit_button.pack()

#Withdraw
withdraw_button = Button(window,
                                text="Withdraw",
                                font=("Arial",10),
                                padx = 16,
                                command=withdraw)
withdraw_button.pack()




window.mainloop()