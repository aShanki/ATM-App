from tkinter import *

root = Tk()
root.title("ATM")
root.geometry("500x500")

frame = Frame(root)
frame.pack()

balance = IntVar()
balance.set(0)
balance_label = Label(frame, text="Current Balance: " + str(balance.get()), font=("Arial", 20), anchor="center")
balance_label.grid(row=0, column=1)

def deposit():
    amount = int(deposit_entry.get())
    balance.set(balance.get() + amount)
    deposit_entry.delete(0, END)

def withdraw():
    amount = int(withdraw_entry.get())
    balance.set(balance.get() - amount)
    withdraw_entry.delete(0, END)

def exit():
    root.destroy()

deposit_label = Label(frame, text="Deposit Amount")
deposit_label.grid(row=1, column=0)

deposit_entry = Entry(frame)
deposit_entry.grid(row=1, column=1)

deposit_button = Button(frame, text="Deposit", command=deposit)
deposit_button.grid(row=1, column=2)

withdraw_label = Label(frame, text="Withdraw Amount")
withdraw_label.grid(row=2, column=0)

withdraw_entry = Entry(frame)
withdraw_entry.grid(row=2, column=1)

withdraw_button = Button(frame, text="Withdraw", command=withdraw)
withdraw_button.grid(row=2, column=2)

exit_button = Button(frame, text="Exit", command=exit)
exit_button.grid(row=3, column=1)


root.mainloop()


