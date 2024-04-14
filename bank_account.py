class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance=${self.balance:.2f}")

    def getBalanced(self):
        print(f"\nAccount '{self.name}' balance=${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposite complete.")
        self.getBalanced()


    def viability(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balnce of ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viability(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete.")
            self.getBalanced()
        except BalanceException as e:
            print(f'\nWithdraw interrupted: {e}')

    def transfer(self, amount, account):
        try:
            print('\n**************************\n\nBeginnig Transfer..')
            self.viability(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Completed!\n\n**************************')
        except BalanceException as e:
            print(f'\nTransfer interrupted: {e}')


class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount + 1.05)
        print("\n Deposite complete.")
        self.getBalanced()


class Savings(InterestRewardAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viability(amount)
            self.balance = self.balance - (amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n Withdraw complete.")
            self.getBalanced()
        except BalanceException as e:
            print(f'\nWithdraw interrupted: {e}')