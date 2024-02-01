from BankAccount import BankAccount

result= BankAccount("Wally", 400)

result.deposit(20.50)

result.withdraw(500)

print(result.get_balance())