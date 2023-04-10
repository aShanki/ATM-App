class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        self.amount = amount
        self.balance = self.balance - self.amount
        return self.balance

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        return self.balance

    def exit(self):
        return "Thank you for using our ATM"

atm = ATM(1000)

def main(atm):
    while True:
        action = input("What would you like to do? (deposit, withdraw, check_balance, exit) ")
        if action == "deposit":
            amount = int(input("How much would you like to deposit? "))
            balance = atm.deposit(amount)
            print(f"Your new balance is {balance}")
        elif action == "withdraw":
            amount = int(input("How much would you like to withdraw? "))
            balance = atm.withdraw(amount)
            print(f"Your new balance is {balance}")
        elif action == "check_balance":
            balance = atm.check_balance()
            print(f"Your balance is {balance}")
        elif action == "exit":
            exit = atm.exit()
            print(exit)
            break
        else:
            print("Invalid action")

main(atm)