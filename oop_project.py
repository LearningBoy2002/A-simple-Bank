from bank_account import *

Dave = BankAccount(1000, "Dave")
Sare = BankAccount(1000, "Sara")

Dave.getBalanced()
Sare.getBalanced()

Sare.deposit(500)


Dave.withdraw(10000)
Dave.withdraw(100)


Dave.transfer(1000, Sare)
Dave.transfer(10, Sare)

Jim = InterestRewardAcct(1000, "Jim")
Jim.getBalanced()
Jim.deposit(100)
Jim.transfer(100, Dave)




Blaze = Savings(1000, "Blaze")

Blaze.getBalanced()

Blaze.deposit(100)

Blaze.transfer(10000, Sare)