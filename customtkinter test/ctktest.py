import customtkinter
from tkinter import IntVar


class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.balance = customtkinter.IntVar()
        self.balance.set(0)
        self.balance_label = customtkinter.CTkLabel(self, text="Current Balance: " + str(self.balance.get()),
                                                    font=("Arial", 20), anchor="center")
        self.balance_label.grid(row=0, column=1)

        self.deposit_label = customtkinter.CTkLabel(self, text="Deposit Amount")
        self.deposit_label.grid(row=1, column=0)

        self.deposit_entry = customtkinter.CTkEntry(self)
        self.deposit_entry.grid(row=1, column=1)

        self.deposit_button = customtkinter.CTkButton(self, text="Deposit", command=self.deposit)
        self.deposit_button.grid(row=1, column=2)

        self.withdraw_label = customtkinter.CTkLabel(self, text="Withdraw Amount")
        self.withdraw_label.grid(row=2, column=0)

        self.withdraw_entry = customtkinter.CTkEntry(self)
        self.withdraw_entry.grid(row=2, column=1)

        self.withdraw_button = customtkinter.CTkButton(self, text="Withdraw", command=self.withdraw)
        self.withdraw_button.grid(row=2, column=2)

        self.exit_button = customtkinter.CTkButton(self, text="Exit", command=self.exit)
        self.exit_button.grid(row=3, column=1)

    def deposit(self):
        amount = int(self.deposit_entry.get())
        self.balance.set(self.balance.get() + amount)
        self.balance_label.configure(text="Current Balance: " + str(self.balance.get()))
        self.entry.delete(0, END)


    def withdraw(self):
        amount = int(self.withdraw_entry.get())
        self.balance.set(self.balance.get() - amount)
        self.balance_label.configure(text="Current Balance: " + str(self.balance.get()))

    def exit(self):
        app.destroy()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.frame = MyFrame(master=self)
        self.frame.pack()

root = customtkinter.CTk()
app = App()
app.mainloop()
